#!/usr/bin/python3


"""Console module for AirBnB project"""


import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB project"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF is reached"""
        print("")  # Add a new line before exiting
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_help(self, arg):
        """do_help function displays documentation"""
        words = "Documented commands (type help <topic>):"
        if arg:
            super().do_help(arg)
        else:
            print("\n{}".format(words), end='\n')
            print('=' * len(words), end='\n')
            for command in self.get_names():
                if command.startswith("do_"):
                    print("{}".format(command[3:]), end=" ")
            print("\n")

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return

        else:
            class_name = arg
            try:
                new_instance = eval(class_name)()
            except NameError:
                print("** class doesn't exist **")
                return
            else:
                new_instance.save()
                print("{}".format(new_instance.id))

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        else:
            class_name = args[0]
            try:
                class_instance = eval(class_name)
            except NameError:
                print("** class doesn't exist **")
                return
            if len(args) == 1:
                print("** instance id missing **")
            else:
                class_id = args[1]
                key = "{}.{}".format(class_name, class_id)
                instance = storage._FileStorage__objects.get(key)
                if instance:
                    print(instance)
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        else:
            class_name = args[0]
            try:
                class_instance = eval(class_name)
            except NameError:
                print("** class doesn't exist **")
                return
            if len(args) == 1:
                print("** instance id missing **")
            else:
                class_id = args[1]
                key = "{}.{}".format(class_name, class_id)
                class_instances = storage._FileStorage__objects.get(key)
                if class_instances:
                    del storage._FileStorage__objects[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """
        Print all string representation of all instances
        """
        args = arg.split()
        if len(args) == 1:
            class_name = args[0]
            try:
                class_instance = eval(class_name)
            except NameError:
                print("** class doesn't exist **")
                return
            instances = storage.all().values()
            filtered_instances = [str(instance) for instance in instances
                                  if isinstance(instance, class_instance)]
            if filtered_instances:
                print(filtered_instances)
            else:
                print("** no instance found **")
        else:
            instances = storage.all().values()
            print([str(instance) for instance in instances])

    def do_update(self, arg):
        """
        Update instances
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        try:
            class_instance = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        else:
            class_id = args[1]
            key = "{}.{}".format(class_name, class_id)
            instance = storage._FileStorage__objects.get(key)
            if instance is None:
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            attr_name = args[2]
            attr_value = args[3]
            if attr_name in ["id", "created_at", "updated_at"]:
                return
            try:
                attr_value = eval(attr_value)
            except (NameError,  SyntaxError):
                pass
            setattr(instance, attr_name, attr_value)
            instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
