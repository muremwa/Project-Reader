from unittest import TestCase, main

from project.folder_reader import KillerFolder, KillerFile, FolderStore, RootDoesNotExist


class KillerFolderTestCase(TestCase):
    def setUp(self):
        self.folder = KillerFolder('king', 'C:\\user\\main')
        self.folder_1 = KillerFolder('queen', 'C:\\user\\main\\queen', parent_folder=self.folder)
        self.folder_2 = KillerFolder('prince', 'C:\\user\\prince', parent_folder=self.folder)
        self.folder_3 = KillerFolder('qu', 'C:\\user\\main\\queen\\qu', parent_folder=self.folder_1)
        KillerFile('one.txt', 45, self.folder)
        KillerFile('two.txt', 45, self.folder)
        KillerFile('three.txt', 45, self.folder)
        KillerFile('four.txt', 45, self.folder_1)
        KillerFile('five.txt', 45, self.folder_1)
        KillerFile('six.txt', 45, self.folder_1)
        KillerFile('seven.txt', 45, self.folder_2)
        KillerFile('eight.txt', 45, self.folder_2)
        KillerFile('nine.txt', 45, self.folder_2)
        KillerFile('ten.txt', 45, self.folder_3)

    def test_parent_folder(self):
        """the parent should be of type Folder"""
        self.assertRaises(ValueError, self.folder.parent_folder, "sd")

    def test__eq__(self):
        """Test comparison of values of KillerFolder"""
        self.assertRaises(TypeError, self.folder.__eq__, 8080)
        fold = KillerFolder("jim", 'C:\\user\\main')
        self.assertEqual(self.folder == fold, True)
        self.assertEqual(self.folder == "C:\\user\\main", True)
        fold.path += "\\jim"
        self.assertEqual(self.folder == fold, False)

    def test_statement(self):
        """Statement of a folder"""
        statement_folder_3 = "\nREADER_FOLDER_LABEL_QU\nten.txt - 45\n---- END OF QU ----"
        statement_folder_2 = "\nREADER_FOLDER_LABEL_PRINCE\nseven.txt - 45\neight.txt - 45\nnine.txt - 45\n---- END " \
                             "OF PRINCE ----"
        statement_folder_1 = "\nREADER_FOLDER_LABEL_QUEEN\nfour.txt - 45\nfive.txt - 45\nsix.txt - 45" + \
                             statement_folder_3 + "\n---- END OF QUEEN ----"
        statement_folder = "\nREADER_FOLDER_LABEL_KING\none.txt - 45\ntwo.txt - 45\nthree.txt - 45" + \
                           statement_folder_1 + statement_folder_2 + "\n---- END OF KING ----"

        self.assertEqual(self.folder.statement(), statement_folder)
        self.assertEqual(self.folder_1.statement(), statement_folder_1)
        self.assertEqual(self.folder_2.statement(), statement_folder_2)
        self.assertEqual(self.folder_3.statement(), statement_folder_3)


class KillerFileTestCase(TestCase):
    def test_path(self):
        """The path of the file should be similar to the parent folder's"""
        folder = KillerFolder('Folder', 'C:\\users\\main')
        file = KillerFile('file', 45, folder)
        self.assertEqual(file.path, folder.path)


class FolderStoreTestCase(TestCase):
    def setUp(self):
        self.folder = KillerFolder('king', 'C:\\user\\main')
        self.folder_1 = KillerFolder('queen', 'C:\\user\\main\\queen', parent_folder=self.folder)
        self.folder_2 = KillerFolder('prince', 'C:\\user\\main\\prince', parent_folder=self.folder)
        self.folder_3 = KillerFolder('qu', 'C:\\user\\main\\queen\\qu', parent_folder=self.folder_1)
        self.folder_store = FolderStore([
            self.folder, self.folder_1, self.folder_2, self.folder_3,
        ])

    def test_init_type_checking(self):
        """
        ensure that when a list is passed during initialization it fails
        if even one object is not a KillerFolder object
        """
        trial = [KillerFolder('name', 'path'), 23]
        self.assertRaises(TypeError, FolderStore, trial)

    def test_store_append(self):
        """the append method should only allow FolderStore objects"""
        self.assertRaises(TypeError, self.folder_store.append, 'string')
        self.assertRaises(TypeError, self.folder_store.append, 3434)
        self.assertRaises(TypeError, self.folder_store.append, [])
        self.assertRaises(TypeError, self.folder_store.append, [self.folder_3])

    def test_folder_fetch(self):
        """the FolderStore.fetch method should return the first instance"""
        self.assertEqual(
            self.folder_store.fetch('C:\\user\\main\\queen\\qu'),
            self.folder_3
        )
        new_folder = KillerFolder('jim', 'C:\\user\\main\\queen\\qu')
        # still the first folder instance
        self.folder_store.append(new_folder)
        self.assertEqual(
            self.folder_store.fetch('C:\\user\\main\\queen\\qu'),
            self.folder_3
        )
        # if new_folder is the first instance
        self.folder_store.insert(1, self.folder_store.pop(-1))
        self.assertEqual(
            self.folder_store.fetch('C:\\user\\main\\queen\\qu'),
            new_folder
        )

    def test_root_statement(self):
        """get statement from the root folder of the store"""
        """Statement of a folder"""
        statement_folder_3 = "\nREADER_FOLDER_LABEL_QU\nten.txt - 45\n---- END OF QU ----"
        statement_folder_2 = "\nREADER_FOLDER_LABEL_PRINCE\nseven.txt - 45\neight.txt - 45\nnine.txt - 45\n---- END " \
                             "OF PRINCE ----"
        statement_folder_1 = "\nREADER_FOLDER_LABEL_QUEEN\nfour.txt - 45\nfive.txt - 45\nsix.txt - 45" + \
                             statement_folder_3 + "\n---- END OF QUEEN ----"
        statement_folder = "\nREADER_FOLDER_LABEL_KING\none.txt - 45\ntwo.txt - 45\nthree.txt - 45" + \
                           statement_folder_1 + statement_folder_2 + "\n---- END OF KING ----"
        KillerFile('one.txt', 45, self.folder)
        KillerFile('two.txt', 45, self.folder)
        KillerFile('three.txt', 45, self.folder)
        KillerFile('four.txt', 45, self.folder_1)
        KillerFile('five.txt', 45, self.folder_1)
        KillerFile('six.txt', 45, self.folder_1)
        KillerFile('seven.txt', 45, self.folder_2)
        KillerFile('eight.txt', 45, self.folder_2)
        KillerFile('nine.txt', 45, self.folder_2)
        KillerFile('ten.txt', 45, self.folder_3)

        self.assertRaises(RootDoesNotExist, self.folder_store.root_statement)
        self.folder_store.__dict__['root'] = "string"
        self.assertRaises(AttributeError, self.folder_store.root_statement)
        # register a root folder
        self.folder_store.__dict__['root'] = self.folder.path
        self.assertEqual(self.folder_store.root_statement(), statement_folder)


if __name__ == '__main__':
    main()
