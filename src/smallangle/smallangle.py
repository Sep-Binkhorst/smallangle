import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def cmd_group():
    pass


@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help='NUMBER of steps you want to take between 0 and 2pi.',
    show_default=True
)

def sin(number):
    """Make a list of sin calculations between 0 and 2pi with size NUMBER.

    NUMBER is the amount of steps you want to take between 0 and 2pi.
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help='NUMBER of steps you want to take between 0 and 2pi',
    show_default=True
)

def tan(number):
    """Make a list of tan calculations between 0 and 2pi with size NUMBER.

    NUMBER is the amount of steps you want to take between 0 and 2pi.
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


if __name__ == "__main__":
    cmd_group()