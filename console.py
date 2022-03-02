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
        """\033[38;2;132;255;161m
        Creates a new instance of BaseModel and storage in JSON file
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
        """\033[38;2;132;255;161m
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
        """ \033[38;2;132;255;161m
        Deletes an instance based on the class name and id
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
            del storage.all()[cls_name + "." + id]

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or updating attribute
        """
        parts = line.split()
        cls_name = parts[0] if len(parts) > 0 else None
        id = parts[1] if len(parts) > 1 else None
        attribute = parts[2] if len(parts) > 2 else None
        value = parts[3] if len(parts) > 3 else None
        if cls_name is None:
            print("** class name missing **")
        elif cls_name != "BaseModel":
            print("** class doesn't exist **")
        elif id is None:
            print("** instance id missing ** ")
        elif (cls_name + "." + id) not in list(storage.all().keys()):
            print("** no instance found **")
        elif attribute is None:
            print("** attribute name missing **")
        elif value is None:
            print("** value missing **")
        else:
            storage.new(cls_name + "." + str(attribute), value)
        
    def do_all(self, line):
        """\033[38;2;132;255;161m
        Prints all string representation of all instances
        based or not on the class name
        """
        if line != "" and line != "BaseModel":
            print("** class doesn't exist **")
        else:
            my_dict = storage.all()
            for key in list(my_dict.keys()):
                print(BaseModel(**my_dict[key]))

    def do_EOF(self, line):
        """\033[38;2;132;255;161m
        Terminates the running program
        Usage:
        (hbnb) 'ctrl + D'
        """
        print()
        return True

    def do_quit(self, line):
        """\033[38;2;132;255;161m
        Quit command to exit the program
        Usage:
        (hbnb)$ quit
        """
        return True

    def do_help(self, arg):
        """\033[38;2;132;255;161m
        Help for commands
        Usage:
        (hbnb)$ help // List available commands
        (hbnb)$ help 'cmd' // Detailed help on the command(cmd)
        """
        # 'Listavailablecommands with "help" or detailed help with "help cmd"'
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        """
        Ignore empty lines
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
