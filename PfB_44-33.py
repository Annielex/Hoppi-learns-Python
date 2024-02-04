# Virtual Environments

# Modules
# are Python files with functions, classes and other components
#that help breaking down code into reusable structures

# Creating a module

# create a file:
# helpers.py
# and add in appropriate code:
def display(message, is_warning=False):
    if is_warning:
        print("Warning!!!")
    print(message)


# Using a module:

# option 1: import module as namespace
import helpers # complete module is imported
helpers.display("Not a warning")

# option 2: import all into current namespace
from helpers import * # * means everything - will import everything inside module helpers
display("Not a warning")

# option 3: import specific items into current namespace
from helpers import display # only the specific item "display" will be imported from helpers
display("Not a warning")

# Packages

# are published collections of modules
# packages can be found on Python Package Index as well as other Internet searches

# Installing packages
# pip is the commandline installer to use for instaling packages

# If you have list of packages - set them up in a text file
# requirements.txt - text inside this file is the list of all the packages reuired to be used
colarama # one package list ;)

# Install an individual package
pip install colorama

# Install from a list of packages
pip install -r requirements.txt # what does the "-r" do?


