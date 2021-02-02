### Setup
## Project Requirements

**pyenv** - to manage python versions

**pipenv** - to manage pip dependencies

_basic breakdown of these two_

`.python-version` in the root of a folder tells **pyenv** what version of python to use

`Pipfile` and `Pipfile.lock` are used by **pipenv** to manage dependencies. `pipenv install --system` will install these dependencies on your system versions of python and pip.

## Setup and usage

# General use

The command will print help and usage when run with no arguments. If this were a working project then the content would be dynamic. Documenting dynamic code outside of the code is a fools game. Instead make sure that it's tightly coupled, the code can provide documentation or at the bare minimum include a link/URL to more indepth content.

If you wish to run this cli from any terminal in any location, then make sure that the main file is available in the shell's path and that the system versions of python and pip dependencies are compatible.

The alternative is to compile this code into a static file, or similar. This is currently out of scope as this repo is intended for developers not yet targeting a user base.

# Updating pip modules or installing new ones

To contribute to this project please use pyenv and pipenv to control the dependencies. These must be setup and a virtualenv can be used to separate this from other python projects.

Activate the correct python version by changing directory to the project root. Note the `.python-version` file that is used by pyenv. This is all that's needed if pyenv is setup correctly. See pyenv docs for more info.

Activate the pip virtualenv - this gives you a workspace to run code with different versions to the system:

    `pipenv shell`

Install or update new modules using:

    `pipenv install module_name` or `pipenv update module_name`

Be sure to sync and lock so that new modules or versions are captured in the Pipfile.lock. These files can then be checked in and picked up by another developer to recreate the same conditions and setup.

    `pipenv update`

# Run it

`cd ~/git` (or where you clone your git repos)

`git clone ... ` <include the ssh or https link to this repo>

`cd click_cli` (change directoy to the cloned repo. Running `python --version` here expect to see the same version as mentioned in `.python-version`, check pyenv install if not)

`pipenv install` (will setup the dependencies required)

`pipenv shell` (will enter the virtualenv for development)

`./click_cli` (this will print the usage and allow you to use the cli tool)

# Contributing

Improvements and suggestions are welcome!

If using in a team and encouraging others to contribute subcommands to this utility then there is an easy pattern to follow.

1. Put the python code into a `.py` file within the `utils` directory (next to `helloworld.py`)
1. Wrap this code with the click references
1. Add an explicit reference to the main file
1. Check and confirm that your new command is available

The existing code will allow wildcard imports from the `utils` folder, as specified in the `__init__.py` so all that is required is working code and the explicit mention in the main python file, click_cli.
