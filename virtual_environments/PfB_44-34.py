# Virtual Environments

# By default packages are installed globally in python which creates challenges for version management

# Virtual Environments can be used to contain and manage collections,
# therefore acting as folder behind the scenes with all the packages

# Creating a virtual environment

# Install virtual environment
pip install virtualenv

# Create the virtual environment depending on your operating system

# Windows systems
python -m venv <folder_name> # -m means "go grab a particular module", venv is short for virtual environment

# OSX/Linux (bash)
virtualenv <folder_name>

# Using virtual environments depending on operating system and on environment

# Windows systems - everything in a subfolder called Scripts and then activate that as per below
# cmd.exe
<folder_name>\Scripts\Activate.bat
# Powershell
<folder_name>\Scripts\Activate.ps1
# bash shell
. ./<folder_name>/Scripts/Activate

# OSX/Linux (bash) - instead of scripts it will be bin
. <folder_name>/bin/activate

# Unstalling packages in a virtual environment
# Installing an individual package
pip install colorama

# Install from a list of packages
pip install -r requirements.txt

# requirements.txt
colorama

