#!/usr/bin/python3
""" Module
        pass
"""
import cmd
import os
import pwd


class HBNBCommand(cmd.Cmd):
    """ Class definition
            pass
    """
    intro = ("\033[38;2;245;97;166m*" * 25) +\
        "\n* Welcome {}\n".format(pwd.getpwuid(os.getuid()).pw_name) +\
        ("*" * 25)
    prompt = "\033[38;2;255;56;92m(HBNB)$\033[0m "

    def emptyline(self):
        pass

    def do_EOF(self, line):
        """ Terminates the running program
        Usage:
        (HBNH)$ 'ctrl + D'
        """
        print()
        return True

    def do_quit(self, line):
        """ Quit command to exit the program
        Usage:
        (HBNB)$ quit
        """
        return True

    def do_help(self, arg):
        """ Help for commands
        Usage:
        (HBNB)$ help // List available commands
        (HBNB)$ help 'cmd' // Detailed help on the command(cmd)
        """
        # 'Listavailablecommands with "help" or detailed help with "help cmd"'
        cmd.Cmd.do_help(self, arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
