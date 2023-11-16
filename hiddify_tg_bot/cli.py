"""CLI interface for hiddify_tg_bot project.

Be creative! do whatever you want!

- Install click or typer and create a CLI app
- Use builtin argparse
- Start a web application
- Import things from your .base module
"""
from bot import BOT,run


def main():  # pragma: no cover
    """
    The main function executes on commands:
    `python -m hiddify_tg_bot` and `$ hiddify_tg_bot `.

    This is your program's entry point.

    You can change this function to do whatever you want.
    Examples:
        * Run a test suite
        * Run a server
        * Do some other stuff
        * Run a command line application (Click, Typer, ArgParse)
        * List all available tasks
        * Run an application (Flask, FastAPI, Django, etc.)
    """

    print(f'Handling {BOT.get_me().username} bot')
    run()

main()