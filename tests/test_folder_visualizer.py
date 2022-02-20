from unittest import TestCase, main

from project.folder_visualizer import Folder, File, assign_classes


class FolderTestCase(TestCase):
    def setUp(self):
        self.folder = Folder("Name")
        self.parent_folder = Folder("Parent")

    def test_parent_folder(self):
        self.assertEqual(type(self.folder.parent_folder).__name__, "NoneType")
        self.assertRaises(ValueError, self.folder.parent_folder, "parent")
        self.folder.parent_folder = self.parent_folder
        self.assertEqual(self.folder.parent_folder.name, self.parent_folder.name)


class AssignClassTestCase(TestCase):
    def setUp(self):
        self.top_folder_name = "FOLDER_GITHUB_PROJECTS_2.txt"
        self.top_folder = Folder(self.top_folder_name.split("FOLDER_")[-1].split(".txt")[0])
        self.idea = Folder('.IDEA', parent_folder=self.top_folder)
        self.dictionaries = Folder('DICTIONARIES', parent_folder=self.idea)
        self.solutions = [
            self.top_folder,
            File('question_1.py', 38, self.top_folder),
            File('question_2(factorial).py', 66, self.top_folder),
            File('question_21.py', 45, self.top_folder),
            self.idea,
            File('github projects 2.iml', 11, self.idea),
            File('misc.xml', 5, self.idea),
            File('modules.xml', 5, self.idea),
            File('workspace.xml', 17, self.idea),
            self.dictionaries,
            File('muremwa.xml', 5, self.dictionaries),
            Folder('DESC', parent_folder=self.top_folder),
        ],

    @staticmethod
    def name_synthesis(klasses):
        for k, klass in enumerate(klasses):
            if type(klass).__name__ == "Folder":
                if klass.parent_folder:
                    klasses[k] = "Folder called {folder_name} with parent {folder_parent}".format(
                        folder_parent=klass.parent_folder.name,
                        folder_name=klass.name,
                    )
                else:
                    klasses[k] = "Folder called {folder_name}".format(folder_name=klass.name)

            elif type(klass).__name__ == "File":
                klasses[k] = "File called {file_name} parent is {parent}".format(
                    file_name=klass.name,
                    parent=klass.parent_folder.name
                )
        return klasses

    def test_solution(self):
        expected = self.name_synthesis(self.solutions[0])
        result = self.name_synthesis(assign_classes(self.top_folder_name))
        self.assertListEqual(expected, result)


if __name__ == '__main__':
    main()
