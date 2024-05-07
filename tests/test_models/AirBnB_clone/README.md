# 0x00. AIRBNB clone - the console

writing a command interpreter to manage your AirBnB Objects.
-it helps to put in place a parent class
-creates a simple flow of serialization/deserialization
-create all classes used for AirBnB(User, State, City, Place..)that inherit from BaseModel
-Create all unittests to validate all our classes and storage engine

DEFINITION OF A COMMAND INTERPRETER
-Creating a new object
-Retrieve an object from a file
-Do operations on objecs(count, compute stats)
-Update attributes of an object
-Destroy an object

##GENERAl requirements of this project
learning how to create a python package
how to create a command interpreterin python while using the cmd module

#all the classes re handled by the 'storage' engine in the 'filestorage' class.
#the code uses the pycodestyle(version 2.8.*)
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
#the shell should work like this in interactive mode:
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
#in the non-interactive mode:
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash


