#!/usr/bin/python3
""" console module """

import cmd
import re
from shlex import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand class:
    Attributes:
        prompt: public attr, str - prompt message
        cls_dict: public attr, dictionay - a dict of classes
    """
    prompt = '(hbnb) '
    cls_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def postloop(self):
        print()

    def do_EOF(self, args):
        """do_EOF: Ctrl+D to exit
        Return:
            return True
        """
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
        all_objs = storage.all()
        if not args:
            print([str(v) for v in all_objs.values()])
        elif arg_list[0] in self.cls_dict:
            print([str(v) for v in all_objs.values() if type(
                v) == self.cls_dict.get(arg_list[0])])
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
                storage.save()
            except BaseException:
                print("** no instance found **")

    def do_update(self, args):
        """do_update: Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON
        file)
        Args:
            args: a string in format: <className> <id> <attribute name>
        "<attribute value>"
        """
        arg_list = args.split(" ", 3)
        all_objs = storage.all()

        if len(arg_list) > 1:
            key = "{}.{}".format(arg_list[0], arg_list[1].strip("'\""))
        if not args:
            print("** class name missing **")
        elif arg_list[0] not in self.cls_dict:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif key not in all_objs:
            print("** no instance found **")
        elif len(arg_list) == 2:
            print("** attribute name missing **")
        elif len(arg_list) == 3:
            print("** value missing **")
        else:
            obj = all_objs.get(key)
            arg_list[3] = list(shlex(arg_list[3]))[0]
            arg_list[2] = arg_list[2].strip("'\"")
            if hasattr(obj, arg_list[2]):
                type_attr = type(getattr(obj, arg_list[2]))
                if type_attr is not str:
                    setattr(obj, arg_list[2], type_attr(arg_list[3]))
                else:
                    arg_list[3] = arg_list[3].strip("'\"")
                    setattr(obj, arg_list[2], arg_list[3])
            else:
                try:
                    arg_list[3] = int(arg_list[3])
                except ValueError:
                    try:
                        arg_list[3] = float(arg_list[3])
                    except ValueError:
                        arg_list[3] = arg_list[3].strip("'\"")
                setattr(obj, arg_list[2], arg_list[3])
            obj.save()

    def default(self, args):
        cmd_list = re.split('[.(),:{}]', args)
        cmd_list = [e.strip() for e in cmd_list]
        cmd_list = [e for e in cmd_list if e != ""]
        if len(cmd_list) < 2:
            print('*** Unknown syntax:', cmd_list[0])
            return False
        if cmd_list[0] not in list(self.cls_dict.keys()):
            print('*** Unknown syntax: {}.{}'.format(
                cmd_list[0], cmd_list[1]))
            return False
        if cmd_list[1] == 'count':
            self.count_model_instance(cmd_list[0])
        if cmd_list[1] == 'all':
            self.do_all(cmd_list[0])
        if cmd_list[1] == 'show':
            self.do_show(cmd_list[0] + ' ' + cmd_list[2])
        if cmd_list[1] == 'destroy':
            self.do_destroy(cmd_list[0] + ' ' + cmd_list[2])
        if cmd_list[1] == 'update':
            key = 3
            while(key != len(cmd_list)):
                self.do_update(" ".join([cmd_list[0], cmd_list[
                    2], cmd_list[key], cmd_list[key + 1]]))
                key = key + 2

    def count_model_instance(self, model):
        all_objs = storage.all()
        models = [v for v in all_objs.values() if type(
            v) == self.cls_dict.get(model)]
        print(len(models))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
