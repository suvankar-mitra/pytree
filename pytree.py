#!/usr/bin/python3
from genericpath import isdir
import os
import sys

import pytree_constant


def print_error(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    exit(1)

class Tree:
    num_dir = -1
    num_file = 0
    num_sym_link = 0

    tree_output = ""
    tree_output_meta = ""

    def traverse_tree(self, dir_name) :
        # check if directory exists
        if not os.path.exists(dir_name):
            print_error("Err: The path does not exist: ",dir_name)
        
        # check if given path is a directory
        if not os.path.isdir(dir_name) :
            print_error("Err: This is not a directory: ",dir_name)

        self.file_walk(dir_name,"","",0)

    def file_walk(self, path: str, space: str, prefix: str, level: int):

        # if os.path.basename(path).startswith(".") and not prefix == "":
            # return
        
        if os.path.isdir(path):
            if prefix == "":
               print(prefix+pytree_constant.ANSI_BLUE+os.path.basename(path)+pytree_constant.ANSI_RESET)
            else:
               print(space[4:]+prefix+" "+pytree_constant.ANSI_BLUE+os.path.basename(path)+pytree_constant.ANSI_RESET)

            k = 0
            dir_list = os.listdir(path)
            dir_list.sort()
            for file in dir_list:
                k += 1
                if k == len(dir_list):
                    if prefix == "├──":
                        self.file_walk(os.path.join(path,file),space+"│"+pytree_constant.SPACE,"└──",0)
                    else:
                        self.file_walk(os.path.join(path,file),space+pytree_constant.SPACE,"└──",0)
                else:
                    if prefix == "├──":
                        self.file_walk(os.path.join(path,file),space+"│"+pytree_constant.SPACE,"├──",0)
                    else:
                        self.file_walk(os.path.join(path,file),space+pytree_constant.SPACE,"├──",0)
                
        else:
            print(space[4:]+prefix+pytree_constant.ANSI_GREEN+os.path.basename(path)+pytree_constant.ANSI_RESET)


# Main

def main():
    if len(sys.argv) < 2 :
        print_error("Please provide at least one directory as argument!")

    for d in sys.argv[1:]:
        Tree().traverse_tree(d)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nInterrupted')
        try:
            sys.exit(2)
        except SystemExit:
            os._exit(2)
