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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
