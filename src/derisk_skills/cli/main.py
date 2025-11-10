"""
    DeRisk Skill CLI Module - Setup tool for OpenDerisk 

    Usage: derisk-cli [OPTIONS] COMMAND [ARGS]...
"""
import typer
import logging
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

BANNER = """

    ____       ____  _      __        _____ __   _ ____    
   / __ \___  / __ \(_)____/ /__     / ___// /__(_) / /____
  / / / / _ \/ /_/ / / ___/ //_/_____\__ \/ //_/ / / / ___/
 / /_/ /  __/ _, _/ (__  ) ,< /_____/__/ / ,< / / / (__  ) 
/_____/\___/_/ |_/_/____/_/|_|     /____/_/|_/_/_/_/____/                                                                                                                  


"""

TAGLINE = "OpenDerisk Skills - Spec-Driven AIOps for Risk Management"


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
    colors = ["bright_blue", "blue", "cyan", "bright_cyan", "white", "bright_white"]

    styled_banner = Text()
    for i, line in enumerate(banner_lines):
        color = colors[i % len(colors)]
        styled_banner.append(line + "\n", style=color)

    console.print(Align.center(styled_banner))
    console.print(Align.center(Text(TAGLINE, style="italic bright_yellow")))
    console.print()

@app.command()
def init():
    """
    Initialize the CLI tool and display the banner 
    """
    show_banner()


@app.command()
def list_skills():
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
    typer.echo(f"Creating a new skill template with name: {name}")


def main():
    app()

if __name__ == "__main__":
    main()