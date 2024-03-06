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
                if command.startswith("do"):
                    print("{}".format(command[3:]), end=" ")
            print("\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
