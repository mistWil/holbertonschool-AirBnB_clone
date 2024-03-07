#!/usr/bin/python3


"""Console module for AirBnB project"""


import cmd
from models import storage
<<<<<<< HEAD
from models.engine.file_storage import FileStorage
=======
>>>>>>> 2a21b5f14dfb6436ad465e9c7ce9a72c488ccdbd
from models.base_model import BaseModel


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
<<<<<<< HEAD
        from models.base_model import BaseModel

        class_name = arg.split()[0] if arg else None

        if not class_name:
            print("** class name missing **")
        elif class_name not in storage.all():
            print("** class doesn't exist **")
        else:
            new_instance = eval(class_name)()
            new_instance.save()
            print(new_instance.id)
=======
        if not arg:
            print("** class name missing **")
            return

        class_name = arg
        try:
            new_instance = eval(class_name)()
        except NameError:
            print("** class doesn't exist **")
            return
        new_instance.save()
        print(new_instance.id)
>>>>>>> 2a21b5f14dfb6436ad465e9c7ce9a72c488ccdbd

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()

        if not args:
<<<<<<< HEAD
            print("class name missing")
=======
            print("** class name missing **")
>>>>>>> 2a21b5f14dfb6436ad465e9c7ce9a72c488ccdbd
            return

        class_name = args[0]

<<<<<<< HEAD
        if class_name not in storage.classes():
            print("class doesn't exist")
            return

        if len(args) < 2:
            print("instance id missing")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        obj_dict = storage.all()

        if key not in obj_dict:
            print("** no instance found **")
            return

        print(obj_dict[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        obj_dict = storage.all()

        if key not in obj_dict:
            print("** no instance found **")
            return

        del obj_dict[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        class_name = args[0] if args else None

        # Récupérer toutes les instances de la classe donnée
        if class_name:
            instances = [obj for key, obj in storage.all().items() if key.startswith(class_name + '.')]
        else:
            instances = storage.all().values()

        # Imprimer la représentation de chaque instance
        if not instances:
            print("** class doesn't exist **")
        else:
            for instance in instances:
                print(instance)


    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        from models import storage

        args = arg.split()

        if len(args) < 3:
            print("Usage: update <class name> <id> <attribute name> '<attribute value>'")
            return

        class_name = args[0]

        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
=======
        try:
            new_instance = eval(class_name)()
        except NameError:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
>>>>>>> 2a21b5f14dfb6436ad465e9c7ce9a72c488ccdbd

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        obj_dict = storage.all()

<<<<<<< HEAD
        # Vérifier si l'instance existe dans le stockage
=======
>>>>>>> 2a21b5f14dfb6436ad465e9c7ce9a72c488ccdbd
        if key not in obj_dict:
            print("** no instance found **")
            return

<<<<<<< HEAD
        attribute_name = args[2]

        # Vérifier si le nom de l'attribut est manquant
        if len(args) < 4:
            print("** attribute name missing **")
            return

        attribute_value = args[3]

        # Mise à jour de l'attribut
        instance = obj_dict[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

=======
        print(obj_dict[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        try:
            new_instance = eval(class_name)()
        except NameError:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        obj_dict = storage.all()

        if key not in obj_dict:
            print("** no instance found **")
            return

        del obj_dict[key]
        storage.save()

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

>>>>>>> 2a21b5f14dfb6436ad465e9c7ce9a72c488ccdbd

if __name__ == '__main__':
    HBNBCommand().cmdloop()
