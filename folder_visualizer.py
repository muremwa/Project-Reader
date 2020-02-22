"""
visualize the hierarchy of a folder in the fashion shown below
TOP_LEVEL_FOLDER
|
|---- file.txt (500 lines)
|
|---- name_file.py (89 lines)
|
|---- 2ND_LEVEL_FOLDER
|           |
|           |---- disc.cpp (40 lines)
|           |
|           |----3RD_LEVEL_FOLDER
|                      |
|                      |--- file.txt (79 lines)
|
|---- 2ND_LEVEL_FOLDER_2
|           |
|           |- file.txt (56 lines)
|

"""


import re


# class to represent a file
class File:
    """
    File class represents a file
    name is the name of the file ends in extension normally. type string
    number_of_lines - number of lines of the file. type integer
    parent folder is the folder the file belongs to. type Folder class
    """
    def __init__(self, name, number_of_lines, parent_folder):
        self.name = name
        self.number_of_lines = int(number_of_lines)
        self.parent_folder = parent_folder

        # make sure the parent_folder is of type "Folder"
        if type(self.parent_folder).__name__ != "Folder":
            raise ValueError("parent folder should be an object of the class Folder")

        self.parent_folder.files.append(self)

    def __str__(self):
        return "{file_name} ({lines} lines)".format(
            lines=self.number_of_lines,
            file_name=self.name,
        )

    def __repr__(self):
        return "{file_name} from the folder {folder}".format(
            folder=self.parent_folder,
            file_name=self.name,
        )


# class to represent a folder
class Folder:
    """
    represents a folder
    name is a string
    the parent is mandatory if the folder is not a parent folder
    i.e. Folder("Folder name", parent_folder=folder_object)
    """
    def __init__(self, name, **kwargs):
        self.name = str(name)
        try:
            self.parent_folder = kwargs['parent_folder']

            # make sure the parent_folder is of type "Folder"
            if type(self.parent_folder).__name__ != "Folder":
                raise ValueError("parent folder should be an object of the class Folder")

        except KeyError:
            self.parent_folder = None
            print("WARNING: If this is not the root folder, please add a parent")

        self.files = []

    def __str__(self):
        return self.name.upper()

    def __repr__(self):
        return self.name.upper()


def assign_classes(top_folder_name):
    """
    Takes all the names representing files and folder and assign them their respective classes

    :param top_folder_name: string representing file name of the text file with all folder and files
    :type top_folder_name: string
    :return: list of objects of File or Folder type
    :rtype: list
    """
    with open(top_folder_name, 'r') as open_file:
        lines = open_file.readlines()

    lines = [line.strip() for line in lines]
    top_folder = Folder(top_folder_name.split("FOLDER_")[-1].split(".txt")[0])
    solution = [top_folder, ]
    parent = top_folder

    # make a list of all folders
    for line in lines:
        if line.islower():
            file_name, no_lines = line.split(" - ")
            solution.append(File(file_name, no_lines, parent))

        elif line.isupper():
            if re.search('END OF', line):
                parent = parent.parent_folder
            else:
                folder = Folder(line, parent_folder=parent)
                solution.append(folder)
                parent = folder

    return solution


def depth_calculator(obj):
    """Determine how far in the hierarchy the file/folder is in. Works for either File or Folder class"""
    depth = 0
    dad = obj.parent_folder
    next_in = True

    while next_in:
        if dad.parent_folder:
            depth += 1
            dad = dad.parent_folder
        else:
            next_in = False

    return depth


# drawing utility
def draw(klasses, **kwargs):
    """
    The function takes in classes and writes to file/draws in a file the hierarchy
    If no file_name is given on is chosen for you

    :param klasses: a list of objects of types File or Folder usually products of "assign_classes" function
    :type klasses: list
    """
    top_folder = klasses[0]
    depth = 10

    top_folder_name = kwargs.get('file_name', '{}.txt'.format(top_folder))

    with open(top_folder_name, 'w') as open_file:
        # first line is the top folder name
        print(top_folder, file=open_file)

        # others
        for klass in klasses[1:]:
            # how far in the hierarchy?
            depth_level = depth_calculator(klass)
            travel = depth * depth_level

            # always an extra line here
            if travel == 0:
                print("|", file=open_file)
            else:
                print("|" + " "*travel + "|", file=open_file)

            # simple file
            if type(klass).__name__ == "File":
                # top level files
                if travel == 0:
                    print("|---- {file}".format(file=str(klass)), file=open_file)

                # more level files
                else:
                    print("|" + " "*travel + "|---- {file}".format(file=str(klass)), file=open_file)

            elif type(klass).__name__ == "Folder":
                # top level folders
                if travel == 0:
                    print("|---- {folder}".format(folder=str(klass)), file=open_file)

                # more level folders
                else:
                    print("|" + " "*travel + "|---- {folder}".format(folder=str(klass)), file=open_file)
