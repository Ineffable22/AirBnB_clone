#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    intro = ("*" * 25) +\
        "\n* Welcome to my Shell\n*" +\
        "\n* Authors:\n*" +\
        "\tMiguel Barrera\n*" +\
        "\tMiguel Grillo\n*" +\
        ("*" * 25)
    prompt = "(HBNB)$"

    def emptyline(self):
        pass
    def do_EOF(self, line):
        return True
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    def do_help(self, arg):
        'List available commands with "help" or detailed help with "help cmd".'
        cmd.Cmd.do_help(self, arg)
            
if __name__ == '__main__':
    HBNBCommand().cmdloop()

