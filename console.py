#!/usr/bin/python3
""" Module
        pass
"""
import cmd
import os
import pwd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd, FileStorage):
    """ Class definition
            pass
    """
    intro = ("\033[38;2;245;97;166m*" * 25) +\
        "\n* Welcome {}\n".format(pwd.getpwuid(os.getuid()).pw_name) +\
        ("*" * 25)
    prompt = "\033[38;2;255;56;92m(hbnb)\033[0m "

    def do_create(self, line):
        """ Creates a new instance of BaseModel and storage in JSON file
        Usage:
        (hbnb) create BaseModel // stdout: id of the instance
        """
        if line == "":
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            obj = BaseModel()
            storage.save()
            print(obj.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        parts = line.split()
        cls_name = parts[0] if len(parts) > 0 else None
        id = parts[1] if len(parts) > 1 else None
        if cls_name is None:
            print("** class name missing **")
        elif cls_name != "BaseModel":
            print("** class doesn't exist **")
        elif id is None:
            print("** instance id missing ** ")
        elif (cls_name + "." + id) not in list(storage.all().keys()):
            print("** no instance found **")
        else:
            print(storage.all()[cls_name + "." + id])

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id"""
        parts = line.split()
        cls_name = parts[0] if len(parts) > 0 else None
        id = parts[1] if len(parts) > 1 else None
        if cls_name is None:
            print("** class name missing **")
        elif cls_name != "BaseModel":
            print("** class doesn't exist **")
        elif id is None:
            print("** instance id missing ** ")
        elif (cls_name + "." + id) not in list(storage.all().keys()):
            print("** no instance found **")
        else:
            del storage.all()[cls_name + "." + id]

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def do_EOF(self, line):
        """ Terminates the running program
        Usage:
        (hbnb) 'ctrl + D'
        """
        print()
        return True

    def do_quit(self, line):
        """ Quit command to exit the program
        Usage:
        (hbnb)$ quit
        """
        return True

    def do_help(self, arg):
        """ Help for commands
        Usage:
        (hbnb)$ help // List available commands
        (hbnb)$ help 'cmd' // Detailed help on the command(cmd)
        """
        # 'Listavailablecommands with "help" or detailed help with "help cmd"'
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        """ Ignore empty lines """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
