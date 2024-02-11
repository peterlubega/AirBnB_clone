#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse_arguments(arg):
    """Parse arguments from the command line."""
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split_arguments(arg)]
        else:
            lexer = split_arguments(arg[:brackets.span()[0]])
            ret_list = [i.strip(",") for i in lexer]
            ret_list.append(brackets.group())
            return ret_list
    else:
        lexer = split_arguments(arg[:curly_braces.span()[0]])
        ret_list = [i.strip(",") for i in lexer]
        ret_list.append(curly_braces.group())
        return ret_list


def split_arguments(arg):
    """Split arguments using shlex.split."""
    return split(arg)


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    valid_classes = {"BaseModel", "User", "State", "City", "Place", "Amenity", "Review"}

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid."""
        arg_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }

        match = re.search(r"\.", arg)
        if match is not None:
            arg_list = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg_list[1])
            if match is not None:
                command = [arg_list[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in arg_dict.keys():
                    call = "{} {}".format(arg_list[0], command[1])
                    return arg_dict[command[0]](call)

        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Create a new class instance and print its id."""
        arg_list = parse_arguments(arg)
        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg_list[0])()
            print(new_instance.id)
            storage.save()

    def do_show(self, arg):
        """Display the string representation of a class instance of a given id."""
        arg_list = parse_arguments(arg)
        obj_dict = storage.all()

        if len(arg_list) < 2:
            print("** class name or instance id missing **")
        elif arg_list[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arg_list[0], arg_list[1])])

    def do_destroy(self, arg):
        """Delete a class instance of a given id."""
        arg_list = parse_arguments(arg)
        obj_dict = storage.all()

        if len(arg_list) < 2:
            print("** class name or instance id missing **")
        elif arg_list[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(arg_list[0], arg_list[1])]
            storage.save()

    def do_all(self, arg):
        """Display string representations of all instances of a given class."""
        arg_list = parse_arguments(arg)
        if arg_list and arg_list[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        else:
            obj_list = [str(obj) for obj in storage.all().values() if not arg_list or arg_list[0] == obj.__class__.__name__]
            print(obj_list)

    def do_count(self, arg):
        """Retrieve the number of instances of a given class."""
        arg_list = parse_arguments(arg)
        count = sum(1 for obj in storage.all().values() if arg_list and arg_list[0] == obj.__class__.__name__)
        print(count)

    def do_update(self, arg):
        """Update a class instance of a given id."""
        arg_list = parse_arguments(arg)
        obj_dict = storage.all()

        if len(arg_list) < 3:
            print("** class name, instance id, or attribute name missing **")
            return False

        if arg_list[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return False

        if "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False

        if len(arg_list) == 3:
            print("** value missing **")
            return False

        obj = obj_dict["{}.{}".format(arg_list[0], arg_list[1])]

        if len(arg_list) == 4:
            self.update_single_attribute(obj, arg_list[2], arg_list[3])
        elif type(eval(arg_list[2])) == dict:
            self.update_with_dictionary(obj, eval(arg_list[2]))

        storage.save()

    def update_single_attribute(self, obj, attribute_name, attribute_value):
        """Update a single attribute of a class instance."""
        if attribute_name in obj.__class__.__dict__.keys():
            value_type = type(obj.__class__.__dict__[attribute_name])
            obj.__dict__[attribute_name] = value_type(attribute_value)
        else:
            obj.__dict__[attribute_name] = attribute_value

    def update_with_dictionary(self, obj, attribute_dict):
        """Update attributes of a class instance using a dictionary."""
        for key, value in attribute_dict.items():
            if key in obj.__class__.__dict__.keys() and type(obj.__class__.__dict__[key]) in {str, int, float}:
                value_type = type(obj.__class__.__dict__[key])
                obj.__dict__[key] = value_type(value)
            else:
                obj.__dict__[key] = value


if __name__ == "__main__":
    HBNBCommand().cmdloop()
