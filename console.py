#!/usr/bin/python3
"""
Creating command interpreter
"""
import cmd
import sys
from models.engine.known_objects import classes, console_methods
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Uses cmd methods to control command interpreter """
    # custom prompt:
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ EOF command to exit the program """
        self.non_interactive_check()
        return True

    @staticmethod
    def non_interactive_check():
        if sys.stdin.isatty() is False:
            print("")

    def emptyline(self):
        """ Does nothing, re-prompts """
        self.non_interactive_check()
        pass

    def do_create(self, arguments):
        """
        Creates a new instance of a class
        saves it (to the JSON file)
        and prints the id.
            Ex: $ create BaseModel
        """
        self.non_interactive_check()
        args = self.arg_string_parse(arguments)
        if self.not_a_class(args["cls_name"]):
            return
        cls = classes[args["cls_name"]]
        new_obj = cls()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, arguments):
        """
        Prints the string representation of an instance
        based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234.
        """
        self.non_interactive_check()
        args = self.arg_string_parse(arguments)
        if self.not_a_class(args["cls_name"]):
            return
        if self.not_an_instance(args["cls_name"], args["inst_id"]):
            return
        key = "{}.{}".format(args["cls_name"], args["inst_id"])
        __objects = storage.all()
        print(__objects[key])

    def do_destroy(self, arguments):
        """ Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234.
        """
        self.non_interactive_check()
        args = self.arg_string_parse(arguments)
        if self.not_a_class(args["cls_name"]):
            return
        if self.not_an_instance(args["cls_name"], args["inst_id"]):
            return
        key = "{}.{}".format(args["cls_name"], args["inst_id"])
        __objects = storage.all()
        del __objects[key]
        storage.save()

    def do_all(self, arguments):
        """
        Prints all string representation of all instances
        based on the class name or not.
        Ex: $ all BaseModel or $ all.
        """
        self.non_interactive_check()
        args = self.arg_string_parse(arguments)
        __objects = storage.all()
        print_list = []
        if args["cls_name"] is None:
            for obj in __objects:
                print_string = "{}".format(__objects[obj].__str__())
                print_list.append(print_string)
        else:
            if self.not_a_class(args["cls_name"]):
                return
            for obj in __objects:
                if obj.split(".")[0] == args["cls_name"]:
                    print_string = "{}".format(__objects[obj].__str__())
                    print_list.append(print_string)
        print(print_list)

    def do_update(self, arguments):
        """
        Updates an instance based on the class name and id
        adds or updates attribute and saves the change into the JSON file
        Ex: update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com".
        """
        self.non_interactive_check()
        args = self.arg_string_parse(arguments)
        if self.not_a_class(args["cls_name"]):
            return
        if self.not_an_instance(args["cls_name"], args["inst_id"]):
            return
        if self.not_an_attribute(args["attr_name"]):
            return
        if self.not_a_value(args["attr_value"]):
            return
        key = "{}.{}".format(args["cls_name"], args["inst_id"])
        __objects = storage.all()
        setattr(__objects[key], args["attr_name"], args["attr_value"])

    @staticmethod
    def arg_string_parse(arguments):
        """
        Splits input string of arguments
        arg order determines type of argument
        and arguments are space delimited

        Expected order:
        0. class name
        1. instance id
        2. attribute name
        3. attribute value
        """
        arg_list = arguments.split()
        args = {}
        if len(arg_list) >= 1:
            args["cls_name"] = arg_list[0]
        else:
            args["cls_name"] = None
        if len(arg_list) >= 2:
            args["inst_id"] = arg_list[1]
        else:
            args["inst_id"] = None
        if len(arg_list) >= 3:
            args["attr_name"] = arg_list[2]
        else:
            args["attr_name"] = None
        if len(arg_list) >= 4:
            args["attr_value"] = arg_list[3]
        else:
            args["attr_value"] = None
        return args

    @staticmethod
    def not_a_class(cls_name):
        """
        Checks if given valid class name argument
        Prints error message if missing or invalid
        """
        if cls_name is None:
            print("** class name missing **")
            return True
        if cls_name not in classes:
            print("** class doesn't exist **")
            return True
        return False

    @staticmethod
    def not_an_instance(cls_name, inst_id):
        """
        Checks if given valid instance id argument
        Prints error message if missing or invalid
        """
        if inst_id is None:
            print("** instance id missing **")
            return True
        key = "{}.{}".format(cls_name, inst_id)
        __objects = storage.all()
        if key not in __objects:
            print("** no instance found **")
            return True
        return False

    @staticmethod
    def not_an_attribute(attr_name):
        """
        Checks if given attribute name argument
        Prints error message if missing
        If exists, attr_name is assumed to be valid
            for this model
        """
        if attr_name is None:
            print("** attribute name missing **")
            return True
        return False

    @staticmethod
    def not_a_value(attr_value):
        """
        Checks if given attribute value argument
        Prints error message if missing
        If exists, attr_valid is assumed to be valid
            for this model, but may require type casting
        """
        if attr_value is None:
            print("** value missing **")
            return True
        return False

    def default(self, line):
        """
        Default behavior for unknown commands.
        Verifies if input is in the format:
            * <class name>.<console method>

        Note:
            If input doesn't fit the format, or the class and method don't
            exist, an error message is printed to the user
        """

        try:
            # split based only on first . character
            arg_list = line.split('.', 1)
            # create a dictionary and store the cls_name
            args = {}
            args["cls_name"] = arg_list[0]
            # split rest of string based only on first ( character
            arg_list = arg_list[1].split('(', 1)
            args["method"] = arg_list[0]
            # split arguments like inst_id, attr_name, and attr_value, if given
            if arg_list[1] == ")":
                arg_list = []
            else:
                # split off instance id and check if arguments are dictionary
                arg_check = arg_list[1].split(', ', 1)
                if len(arg_check) > 1:
                    # if dictionary, send to special parsing method
                    if arg_check[1][0] == '{' and args["method"] == "update":
                        arg_string = args["cls_name"]
                        arg_string += " " + arg_check[0] + " " + arg_check[1]
                        self.update_dictionary(arg_string)
                        return
                # if not a dictionary, keep parsing
                arg_string = arg_check[0]
                if len(arg_check) > 1:
                    arg_string += ", " + arg_check[1]
                arg_list = arg_string.split(', ')
                # chops off last ) character
                arg_list[-1] = arg_list[-1][:-1]
            # all code below splices off first and last "" characters
            if len(arg_list) >= 1:
                args["inst_id"] = arg_list[0][1:-1]
            else:
                args["inst_id"] = None
            if len(arg_list) >= 2:
                args["attr_name"] = arg_list[1][1:-1]
            else:
                args["attr_name"] = None
            if len(arg_list) >= 3:
                args["attr_value"] = arg_list[2][1:-1]
            else:
                args["attr_value"] = None
        except:
            self.non_interactive_check()
            print("** Unknown syntax: " + line)
            return

        # validate method
        if args["method"] not in console_methods:
            print("** unsupported method: " + args["method"] + " **")
            return
        if args["method"] == "count":
            method = getattr(self, args["method"])
            self.non_interactive_check()
            method(args["cls_name"])
            return

        method_str = "do_" + args["method"]
        method = getattr(self, method_str)

        arguments = args["cls_name"]
        if args["inst_id"] is not None:
            arguments += " " + args["inst_id"]
        if args["attr_name"] is not None:
            arguments += " " + args["attr_name"]
        if args["attr_value"] is not None:
            arguments += " " + args["attr_value"]

        method(arguments)

    @staticmethod
    def count(cls_name):
        """ Returns the number of instances of cls_name """

        count = 0
        for id, instance in storage.all().items():
            if id.split('.')[0] == cls_name:
                count += 1
        print(count)

    def update_dictionary(self, arguments):
        """
        Parses and runs update method for dictionary args
        for each attribute name/value pair
        """
        # split off class name and instance id
        arg_list = arguments.split(" ", 2)
        args = {}
        args["cls_name"] = arg_list[0]
        args["inst_id"] = arg_list[1][1:-1]
        # cut off dictionary {} and closing ) characters
        dict_string = arg_list[2][1:-2]
        # split the key/value pairs into list of strings
        dictionary = dict_string.split(", ")
        method = getattr(self, "do_update")
        # for each key/value pair in list
        for i in range(len(dictionary)):
            arguments = args["cls_name"] + " " + args["inst_id"] + " "
            # split key and value and set as strings to be added to arguments
            dict_kv = dictionary[i].split(": ")
            args["attr_name"] = dict_kv[0][1:-1]
            if dict_kv[1][0] == "'" and dict_kv[1][-1] == "'":
                dict_kv[1] = dict_kv[1][1:-1]
            args["attr_value"] = dict_kv[1]
            arguments += args["attr_name"] + " " + args["attr_value"]
            # pass arguments to update method
            method(arguments)
        return

if __name__ == "__main__":
    HBNBCommand().cmdloop()
