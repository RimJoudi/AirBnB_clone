#!/usr/bin/python3
"""
console module
"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.review import Review
from models.place import Place


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class
    """

    prompt = "(hbnb) "
    classes = {"BaseModel", "User", "Amenity",
               "State", "City", "Place", "Review"}

    def do_quit(self, args):
        """
        quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """
        EOF command to exit the program
        """
        return True

    def do_help(self, args):
        """
        help command
        """
        cmd.Cmd.do_help(self, args)

    def emptyline(self):
        """
        ignores the empty line and
        prints the prompt again
        """
        pass

    def do_create(self, args):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        """
        args = args.split(" ")
        if args == "":
            print("** class name missing **")
        if args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new = eval("{}()".format(args[0]))
            new.save()
            print(new.id)

    def do_show(self, args):
        """
        Prints the string representation of
        an instance based on the class name and id
        """
        args = args.split()
        if args == "":
            print("** class name missing **")
        if args[0] not in self.classes:
            print("** class doesn't exist **")
        if len(args) < 2:
            print("** instance id missing **")
        else:
            objects = models.storage.all()
            key = "{}.{}".format(args[0], args[1])
            try:
                obj = objects[key]
                print(obj)
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and
        id (save the change into the JSON file)
        """
        if not args:
            print("** class name missing **")
            return
        tokens = args.split(" ")
        objects = models.storage.all()

        if tokens[0] in self.classes:
            if len(tokens) < 2:
                print("** instance id missing **")
                return
            name = tokens[0] + "." + tokens[1]
            if name not in objects:
                print("** no instance found **")
            else:
                obj = objects[name]
                if obj:
                    objs = models.storage.all()
                    del objs["{}.{}".format(type(obj).__name__, obj.id)]
                    models.storage.save()
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        objects = models.storage.all()
        list = []
        if not args:
            for name in objects.keys():
                obj = objects[name]
                list.append(str(obj))
            print(list)
            return
        args = args.split(" ")
        if args[0] in self.classes:
            for name in objects:
                if name[0:len(args[0])] == args[0]:
                    obj = objects[name]
                list.append(str(obj))
            print(list)
        else:
            print("** class doesn't exist **")
            return

    def do_update(self, args):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file).
        """
        args = args.split()
        objects = models.storage.all()
        if args == "":
            print("** class name missing **")

        if args[0] not in self.classes:
            print("** class doesn't exist **")

        if len(args) < 2:
            print("** instance id missing **")

        else:
            k = "{}.{}".format(args[0], args[1])
            if k in objects:
                if len(args) < 3:
                    print("** attribute name missing **")
                if len(args) < 4:
                    print("** value missing **")
                else:
                    obj = objects[k]
                    setattr(obj, args[2], args[3])
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
