#!/usr/bin/python3
"""
User this module for instance shell simulator objects
(HBNB console)

Classes
-------
HBNBCommand
"""
import cmd
import ast  # For to use literal_eval method to convert from string to dict
import re  # for to use regx
from models import storage
from models import cls_dict


class HBNBCommand(cmd.Cmd):
    """
    Template for instances that inherit from the Cmd class in the cmd module,
    so you can run a console
    """
    prompt = "(hbnb) "

    def do_create(self, line):
        """Creates a new instance of BaseModel and storage in JSON file"""
        parts = line.split()
        if self.check_conditions(parts, 1):
            obj = cls_dict[parts[0]]()
            storage.save()
            print(obj.id)

    def do_show(self, line):
        """Prints the string representation of an instance"""
        parts = line.split()
        if self.check_conditions(parts, 2):
            print(storage.all()[parts[0] + "." + parts[1]])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        parts = line.split()
        if self.check_conditions(parts, 2):
            del storage.all()[parts[0] + "." + parts[1]]

    def do_update(self, line):
        """Updates an instance(add or set attribute)"""
        parts = line.split()
        if self.check_conditions(parts, 4):
            setattr(
                storage.all()[parts[0] + "." + parts[1]],  # object
                parts[2],  # attribute
                parts[3]  # value
            )
            storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances by classname"""
        parts = line.split()
        cls_name = parts[0] if len(parts) > 0 else None
        if cls_name is not None and cls_name not in cls_dict.keys():
            print("** class doesn't exist **")
        else:
            if cls_name is None:
                print([str(elm) for elm in storage.all().values()])
            else:
                print([
                    str(elm) for elm in storage.all().values()
                    if elm.__class__.__name__ == cls_name
                ])

    def precmd(self, line):
        """
        Format user input before executing the command, to direct them
        to already existing commands

        Parameter
        ---------
            line : str
                Input of the user from the console
        """
        if re.search('^[A-Z].*\\..*\\(.*\\)$', line):
            parts = (re.split("[.()]", line))[:-1]
            params = parts[2]
            if parts[1] == "update":
                if re.search("[\\{\\}]", params):
                    parts[1] = "d" + parts[1]
                    params = re.split("[,\\s?]", params, 1)
                else:
                    params = re.split("[,\\s?]", params, 2)
                if (parts[1] != "dupdate"):  # some
                    params = list(map(lambda e: e.replace("\"", ""), params))
                params[0] = params[0].replace("\"", "")  # everyone
                params = " ".join(params)
            elif parts[1] != "all" and parts[1] != "count":
                params = params.replace("\"", "")
            line = "{} {} {}".format(parts[1], parts[0], params)
        return line

    def do_dupdate(self, line):
        """\033[38;2;132;255;161m
        Updates an instance based on the class name and id by adding
        or updating passed attributes in a dictionary

        Usage:
            (hbnb) <classname>.update("<id>", <dicttionary>)
        """
        parts = line.split(" ", 2)
        if self.check_conditions(parts, 2):
            my_dict = ast.literal_eval(parts[2])  # dict: Contains attributes
            if not my_dict:
                print("** Wrong dictionary fromat **")
            else:
                for key, value in my_dict.items():
                    setattr(
                        storage.all()[parts[0] + "." + parts[1]],
                        key,
                        value)
                storage.save()

    def do_count(self, line):
        """\033[38;2;132;255;161m
        Shows the number of instances por class

        Usage:
            (hbnb) <classname>.count()
            (hbnb) count <classname>
        """
        parts = line.split()
        if (len(parts) != 1):
            cmd.Cmd.do_help(self, "count")
        else:
            count = 0
            cls_name = parts[0]
            for value in storage.all().values():
                if value.__class__.__name__ == cls_name:
                    count += 1
            print(count)

    def do_EOF(self, line):
        """\033[38;2;132;255;161mTerminates the running program\033[m"""
        print("")
        return True

    def do_quit(self, line):
        """\033[38;2;132;255;161mQuit command to exit the program\033[m"""
        print("")
        return True

    def emptyline(self):
        """
        Ignore empty lines
        """
        pass

    def check_conditions(self, parts, count):
        """
        Validates if the parameters required for the operation
        of the executing command were passed

        Parameters
        ----------
            parts : list
                Contains the parameters
            count : int
                Limit of the validations
        Return
        ------
            band : bool
                true if it was successful
                False if unsuccessful
        """
        # -1:command, 0:class, 1:id, 2:attribute, 3:value
        size = len(parts)
        band = True
        if count > 0:
            if size == 0:
                print("** class name missing **")
                band = False
            elif parts[0] not in cls_dict.keys():
                print("** class doesn't exist **")
                band = False
        if count > 1 and band:
            if size == 1:
                print("** instance id missing ** ")
                band = False
            elif (parts[0] + "." + parts[1]) not in list(storage.all().keys()):
                print("** no instance found **")
                band = False
        if count > 2 and band and size == 2:
            print("** attribute name missing **")
            band = False
        if count > 3 and band and size == 3:
            print("** value missing **")
            band = False
        return band


if __name__ == '__main__':
    HBNBCommand().cmdloop()
