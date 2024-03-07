#!/usr/bin/python3
"""Console module for AirBnB project"""

import cmd
from models import storage
from models.engine.file_storage import FileStorage
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
        """do_help function displays documantation"""
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

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()

        if not args:
            print("class name missing")
            return

        class_name = args[0]

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

        instance_id = args[1]

        # Obtenir l'instance du stockage
        key = "{}.{}".format(class_name, instance_id)
        obj_dict = storage.all()

        # Vérifier si l'instance existe dans le stockage
        if key not in obj_dict:
            print("** no instance found **")
            return

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()