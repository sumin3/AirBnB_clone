#!/usr/bin/python3
""" console module """

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand class:
    Attributes:
        prompt: public attr, str - prompt message
        cls_dict: public attr, dictionay - a dict of classes
    """
    prompt = '(hbnb) '
    cls_dict = {
        "BaseModel": BaseModel
    }

    def do_EOF(self, args):
        """do_EOF: Ctrl+D to exit
        Return:
            return True
        """
        print()
        return True

    def do_quit(self, args):
        """do_quit: input quit to exit
        Return:
            return True
        """
        return True

    def emptyline(self):
        """emptyline: an empty line + ENTER shouldn’t execute
        anything
        """
        pass

    def do_create(self, args):
        """create method: Creates a new instance of input class,
        saves it (to the JSON file) and prints the id
        Args:
           args: the name of the class
        """
        arg_list = args.split()
        if not args:
            print("** class name missing **")
        elif arg_list[0] not in self.cls_dict:
            print("** class doesn't exist **")
        else:
            new_model = self.cls_dict.get(arg_list[0])()
            new_model.save()
            print(new_model.id)

    def do_show(self, args):
        """do_show: Prints the string representation of an instance
        based on the class name and id
        Args:
            args: a string in format: <className> <id>
        """
        arg_list = args.split()
        if not args:
            print("** class name missing **")
        elif arg_list[0] not in self.cls_dict:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            key = "{}.{}".format(arg_list[0], arg_list[1])
            try:
                print(all_objs[key])
            except:
                print("** no instance found **")

    def do_all(self, args):
        """do_all: Prints all string representation of all instances
        based or not on the class name.
        Args:
            args: a string in format: <className>
        """
        arg_list = args.split()
        if not args or arg_list[0] in self.cls_dict:
            all_objs = storage.all()
            print([str(v) for v in all_objs.values()])
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """do_destroy: Deletes an instance based on the class name and id
        Args:
            args: a string in format: <className> <id>
        """
        arg_list = args.split()
        if not args:
            print("** class name missing **")
        elif arg_list[0] not in self.cls_dict:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            key = "{}.{}".format(arg_list[0], arg_list[1])
            try:
                del(all_objs[key])
            except:
                print("** no instance found **")

    def do_update(self, args):
        """do_update: Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON
        file)
        Args:
            args: a string in format: <className> <id> <attribute name>
        "<attribute value>"
        """
        arg_list = args.split()
        all_objs = storage.all()
        if not args:
            print("** class name missing **")
        elif arg_list[0] not in self.cls_dict:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in all_objs:
            print("** no instance found **")
        elif len(arg_list) == 2:
            print("** attribute name missing **")
        elif len(arg_list) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(arg_list[0], arg_list[1])
            setattr(all_objs.get(key), arg_list[2], arg_list[3])
            all_objs.get(key).save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
