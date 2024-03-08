# *``AirBnB clone -``*
This project is a simplified version of the AirBnB website, focusing on creating a command-line interpreter that mimics some of the functionalities of the AirBnB website.

## Command Interpreter Description
The command interpreter, console.py, allows users to interact with the system through a command-line interface. It provides functionality to create, show, destroy, update, and list instances of various classes, such as BaseModel and User.

## REQUIREMENT

Python scripts should be used.
Editors allowed are vi, vim, and emacs.
All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5.
Each file should end with a new line.
The first line of all files should be exactly #!/usr/bin/python3.
A README.md file at the root of the project folder is mandatory.
Code should follow PEP 8 style guide (pycodestyle version 2.7.*).
All files must be executable.
The length of files will be tested using wc.
All modules, classes, and functions should have documentation.
Documentation should be meaningful sentences explaining the purpose (length will be verified).

## How to Start
To start the command interpreter, simply run console.py in your terminal:
$ ./console.py
How to Use
Once the command interpreter is running, you can use the following commands:

##Execution
Your shell should work like this in interactive mode:

$ ./console.py
```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
## COMMAND

`create`: Creates a new instance of a specified class.

`show`: Prints the string representation of an instance based on the class name and ID.

`destroy`: Deletes an instance based on the class name and ID.

`all`: Prints all string representations of instances based on the class name.

`update`: Updates an instance based on the class name and ID by adding or updating attributes.

## EXAMPLES
- `create BaseModel`: This command will create a new instance of the BaseModel class, save it to the JSON file, and print its ID.

```bash
(hbnb) create BaseModel
fa0636af-8e8a-4642-961c-5c83a23d8d0d
(hbnb)
(hbnb) all MyModel
```
- 'Lors de la commande `show BaseModel 1234-1234-1234`', cela affiche la représentation en chaîne d'une instance en fonction du nom de la classe et de l'identifiant.
- 'En exécutant la commande `destroy BaseModel 1234-1234-1234`', cela supprime une instance en fonction du nom de la classe et de l'identifiant.
```
** class doesn't exist **
all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
```

## User Class
A new class, User, has been added to the project, which inherits from BaseModel. It has public class attributes: email, password, first_name, and last_name.

## FileStorage Update
The FileStorage module has been updated to manage serialization and deserialization of User instances correctly.

## Additional Commands
The command interpreter has been updated to allow show, create, destroy, update, and all commands to be used with the User class.

## Testing
Testing scripts have been provided to verify the functionality of the User class and the updated command interpreter.

## Updates
The command interpreter has been updated to include the commands mentioned above. The error management follows the rules specified in the project description.

No unit tests are needed for this project.

## Repo
GitHub repository: https://github.com/mistWil/holbertonschool-AirBnB_clone.git

File: console.py
