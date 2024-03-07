#!/usr/bin/python3
"""Console module for AirBnB project"""

import cmd


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
        
        if not arg:
            print("class name missing")
        elif arg[0] != "BaseModel":
            print("class doesn't exist")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        from models import storage

        if not arg:
            print("class name missing")

        """le nom de la classe existe ?"""
        args = arg.split()
        class_name = args[0]

        if class_name != "BaseModel":
            print("class doesn't exist")

        """on vérifie si l'id est donné"""
        if len(args) < 2:
            print("instance id missing")

        # Obtenir l'ID de l'instance
        instance_id = args[1]

        # Obtenir l'instance du stockage
        key = "{}.{}".format(class_name, instance_id)
        obj_dict = storage.all()

        # Vérifier si l'instance existe dans le stockage
        if key not in obj_dict.keys():
            print("** no instance found **")

        # Imprimer la représentation de l'instance
        print(obj_dict[key])

        def do_destroy(self, arg):
            """Deletes an instance based on the class name and id (save the change into the JSON file)."""
        from models import storage
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        obj_key = "{}.{}".format(class_name, obj_id)
        if obj_key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[obj_key]
        storage.save()


    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name."""
        from models import storage
        objects = storage.all()

        if arg:
            args = arg.split()
            if args[0] not in storage.classes:
                print("** class doesn't exist **")

            objects = {k: v for k, v in objects.items() if k.startswith(args[0])}

        print([str(obj) for obj in objects.values()])

    def do_update(self, arg):
        """ Updates an instance based on the class name and id by adding or updating attribute."""
        from models import storage
        if not arg:
            print("** class name missing **")

        args = arg.split()
        class_name = args[0]
        if class_name not in storage.classes:
            print("** class doesn't exist **")

        if len(args) < 2:
            print("** instance id missing **")

        obj_id = args[1]
        obj_key = "{}.{}".format(class_name, obj_id)
        if obj_key not in storage.all():
            print("** no instance found **")

        if len(args) < 3:
            print("** attribute name missing **")

        if len(args) < 4:
            print("** value missing **")

        attr_name = args[2]
        attr_value = args[3]

        obj = storage.all()[obj_key]
        setattr(obj, attr_name, attr_value)
        obj.save()



if __name__ == '__main__':
    HBNBCommand().cmdloop()