"""
    DeRisk Skill CLI Module - Setup tool for OpenDerisk 

    Usage: derisk-cli [OPTIONS] COMMAND [ARGS]...
"""

import os
import typer
import shutil
import logging
from pathlib import Path

from typer.core import TyperGroup
from rich.console import Console
from rich.text import Text
from rich.align import Align
from typer.core import TyperGroup

from derisk_skills.skills import SKILLS

logging.basicConfig(
    level=logging.WARNING,
    encoding="utf-8",
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger("derisk_cli")

ROOT_PATH = Path(__file__).parent.parent.parent.parent.resolve()


BANNER = r"""
    ____            _      __         _________ 
   / __ \\___  _____(_)____/ /__      / ____/ (_)
  / / / / _ \\/ ___/ / ___/ //_/_____/ /   / / / 
 / /_/ /  __/ /  / (__  ) ,< /_____/ /___/ / /  
/_____/\\___/_/  /_/____/_/|_|      \\____/_/_/ 

"""

TAGLINE = "OpenDerisk Skills - Spec-Driven AIOps Skills for Risk Management"


class BannerGroup(TyperGroup):
    """Custom group that shows banner before help."""

    def format_help(self, ctx, formatter):
        # Show banner before help
        show_banner()
        super().format_help(ctx, formatter)
        
app = typer.Typer(
    name="derisk-cli",
    help="CLI tool for managing OpenDerisk Skills",
    add_completion=False,
    invoke_without_command=True,
    cls=BannerGroup,
)

console = Console()

def show_banner():
    """Display the ASCII art banner."""
    banner_lines = BANNER.strip().split('\n')
    colors = ["bright_blue", "blue", "cyan", "bright_cyan", "red", "bright_red"]

    styled_banner = Text()
    for i, line in enumerate(banner_lines):
        color = colors[i % len(colors)]
        styled_banner.append(line + "\n", style=color)
    
    console.print()

@app.command()
def init():
    """
    Initialize the CLI tool and display the banner 
    """
    show_banner()


@app.command()
def list():
    """
    List all skills
    """
    if len(SKILLS) == 0:
        typer.echo("No skills available.")
        return

    typer.echo("Available Skills:")
    for skill in SKILLS:
        typer.echo(f"- {skill['name']}: {skill['description']}")


# Create a new Typer app for the "new" command
new_app = typer.Typer(help="Create a new skill template")
app.add_typer(new_app, name="new")

@new_app.command("skill")
def new_skill(name: str):
    """
    Create a new skill.
    """
    base_path = os.path.join(
        ROOT_PATH, "src/derisk_skills", "skills", name
    )

    template_path = os.path.join(
        ROOT_PATH, "src/_template", "default_skill_template"
    )

    if os.path.exists(base_path):
        typer.confirm(f"The skill directory '{base_path}' already exist. Do you want to overwrite it?", abort=True)
        shutil.rmtree(base_path)
    
    # Copy template directory to new skill directory
    copy_template_files(template_path, base_path, name)
    typer.echo(f"New skill {name} created successfully at {base_path} from template.")


    typer.echo(f"Creating a new skill template with name: {name}")

@new_app.command("agent")
def new_agent(name: str):
    """
    Create a new agent.
    """
    
    base_path = os.path.join(
        ROOT_PATH, "src/derisk_skills", "agents", name
    )

    template_path = os.path.join(
        ROOT_PATH, "src/_template", "default_agent_template"
    )

    if  os.path.exists(base_path):
        typer.confirm(f"The agent directory '{base_path}' already exist. Do you want to overwrite it?", abort=True)
        shutil.rmtree(base_path)
    
    # Copy template directory to new agent directory
    copy_template_files(template_path, base_path, name)
    typer.echo(f"New agent {name} created successfully at {base_path} from template.")


# Registry skills to OpenDeRisk
@app.command("register")
def register():
    """
    Register skills to OpenDeRisk platform.
    """
    typer.echo("Registering skills to OpenDeRisk platform...")
    for skill in SKILLS:
        typer.echo(f"Registered skill: {skill['name']}")

def copy_template_files(src_dir: str, dst_dir: str, app_name: str):
    for root, dirs, files in os.walk(src_dir):
        dirs[:] = [d for d in dirs if not _should_ignore(d)]
        
        relative_path = os.path.relpath(root, src_dir)
        if relative_path == ".":
            relative_path = ""

        target_dir = os.path.join(dst_dir, relative_path)
        os.makedirs(target_dir, exist_ok=True)

        # Copy all files from the current root to the target directory
        for file in files:
            if _should_ignore(file):
                continue
            
            src_file = os.path.join(root, file)
            dst_file = os.path.join(target_dir, file)
            shutil.copy2(src_file, dst_file) # copy2 preserves metadata


def _should_ignore(file_or_dir: str):
    """Return True if the given file or directory should be ignored.""" ""
    ignore_patterns = [".pyc", "__pycache__"]
    return any(pattern in file_or_dir for pattern in ignore_patterns)


def main():
    app()

if __name__ == "__main__":
    main()