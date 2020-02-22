import os

import folder_visualizer


class RootDoesNotExist(Exception):
    """Exception for when the FolderStore has not root registered"""
    pass


class KillerFolder(folder_visualizer.Folder):
    """Subclass of Folder with extended function"""
    def __init__(self, name, path, **kwargs):
        self.path = path
        super().__init__(name, **kwargs)

    def __eq__(self, other):
        if type(other) not in [__class__, str]:
            raise TypeError('Can only compare with a KillerFolder object')

        if type(other) == __class__:
            if self.path == other.path:
                return True

        elif type(other) == str:
            if self.path == other:
                return True

        return False

    def statement(self):
        """
        returns the folder's statement
        in a string it lists all of its files and folders
        + it adds the statements of the folder's folders who in turn returns the statement of their children folder
        it's a cycle or probably RECURSION or just a LOOP. I'm not sure.
        """
        files = "\n".join([
            "{} - {}".format(file.name, file.number_of_lines) for file in self.files
        ])

        children = []

        for folder in self.folders:
            children.append(folder.statement())

        solution = "\n{folder_name}\n{files}{child}\n---- END OF {folder_name} ----".format(
            folder_name=self.name.upper(),
            files=files,
            child="".join(children),
        )

        return solution


class KillerFile(folder_visualizer.File):
    """Subclass of File with extended function"""
    def __init__(self, name, number_of_lines, parent_folder):
        # KillerFile parent should be KillerFolder
        if not isinstance(parent_folder, KillerFolder):
            raise ValueError("KillerFile's parent should be an instance of KillerFolder")

        super().__init__(name, number_of_lines, parent_folder)

    @property
    def path(self):
        return self.parent_folder.path


class FolderStore(list):
    """Extend the built in list object to create store for Folders"""
    def __init__(self, *args):
        # make sure all items are only KillerFolder items
        if len(args) > 0:
            for item in args[0]:
                if not isinstance(item, KillerFolder):
                    raise TypeError('Items added must be KillerFolder objects: {}'.format(str(item)))
        super().__init__(*args)

    def fetch(self, path):
        """Fetches the 1st occurrence of KillerFolder object with the same path"""
        for killer in self:
            if killer == path:
                return killer

    def append(self, item):
        """Cannot append a non-KillerFolder object"""
        if not isinstance(item, KillerFolder):
            raise TypeError("Can only append objects of KillerFolder")
        return super().append(item)

    def root_statement(self):
        """Returns the statement from the root folder"""
        try:
            root = self.fetch(self.__dict__['root'])
            return root.statement()
        except KeyError:
            raise RootDoesNotExist


def kill_project(path):
    """Takes path of a project and returns a string that can be used to visualize the project"""
    home = os.getcwd()
    os.chdir(path)
    klasses = FolderStore()

    for k, packet in enumerate(os.walk(os.getcwd())):
        path = packet[0]
        parent_path = "\\".join(path.split("\\")[:-1])
        name = path.split("\\")[-1]

        # create KillerFolder
        if k == 0:
            # for the root folder
            k_folder = KillerFolder(name, path)
            klasses.__dict__['root'] = path
        else:
            k_folder = KillerFolder(name, path, parent_folder=klasses.fetch(parent_path))

        # create all files
        for file in packet[-1]:
            KillerFile(file, 0, k_folder)

        klasses.append(k_folder)

    # go back home
    os.chdir(home)
    return klasses.root_statement()


def print_statement(statement):
    """Takes the statement and writes it to file"""
    seq = statement.split("\n")

    # file name is the second in the sequence
    file_name = ("FOLDER " + seq[1]).translate(
        str.maketrans(' ', '_')
    ) + ".txt"

    # write the statement to file
    with open(file_name, 'w') as f:
        print("\n".join(seq[2:-1]), file=f)
