# Demo: Virtual Environment Packages

import helpers # complete import of package
helpers.display("Sample message", True)

# from helpers import * # complete import from package
from helpers import display # individual import from package
display("Sample message")

# Set up virtual environment and install package into that virtual environment

# python -m venv .venv # first venv is the command, the second venv is the folder I am creating
# . .venv/bin/activate # activate virtual environmanet
