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
        pass
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()