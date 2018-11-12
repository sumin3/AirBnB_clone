#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_EOF(self, args):
        """exit"""
        return True

    def do_quit(self, args):
        """exit"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, args):
        """create method: Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        Args:
           args: user input
        """
        if args:
            if args == "BaseModel":
                new_model = BaseModel()
                new_model.save()
                print(new_model.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, args):
        """ show object """
        if args:
            arg_list = args.split()
            if arg_list[0] == "BaseModel":
                if len(arg_list) == 1:
                    print("** instance id missing **")
                else:
                    all_objs = storage.all()
                    for k, obj in all_objs.items():
                        k_list = k.split('.')
                        if k_list[1] == arg_list[1]:
                            print(obj)
                            return
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, args):
        """print all object """
        arg_list = args.split()
        if not args or arg_list[0] == "BaseModel":
            all_objs = storage.all()
            print([str(v) for v in all_objs.values()])
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """destroy an object """
        if args:
            arg_list = args.split()
            if arg_list[0] == "BaseModel":
                if len(arg_list) == 1:
                    print("** instance id missing **")
                else:
                    all_objs = storage.all()
                    for k, obj in all_objs.items():
                        k_list = k.split('.')
                        if k_list[1] == arg_list[1]:
                            all_objs.pop(k)
                            storage.save()
                            return
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_update(self, args):
        """ update """
        if args:
            arg_list = args.split()
            if arg_list[0] == "BaseModel":
                if len(arg_list) == 1:
                    print("** instance id missing **")
                else:
                    all_objs = storage.all()
                    for k, obj in all_objs.items():
                        k_list = k.split('.')
                        if k_list[1] == arg_list[1]:
                            attr_list = {arg_list[2]: arg_list[3]}
                            obj.__init__(**attr_list)
                            storage.save()
                            return
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
