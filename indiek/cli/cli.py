"""
ik
 
Usage:
  ik hello
  ik bye
  ik -h | --help
  ik --version
 
Options:
  -h --help                         Show this screen.
  --version                         Show version.
 
Examples:
  ik hello
  ik bye
 
Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/indiek/indiek.cli
"""
 
 
from inspect import getmembers, isclass
 
from docopt import docopt
 
from . import __version__ as VERSION
 
 
def main():
    """Main CLI entrypoint."""
#    import sys
#    print(sys.path)
    import indiek.cli.commands as commands
    options = docopt(__doc__, version=VERSION)
#    print(options)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for k, v in options.items():
        if v and hasattr(commands, k):
 #           print(k)
            module = getattr(commands, k)
            commands = getmembers(module, isclass)
            command = [command[1] for command in commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
