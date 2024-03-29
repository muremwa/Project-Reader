Project Reader
==============

Read and summarize the files in your projects. An easy way to achieve
the following:

1. Count the number of lines in your project.
2. Visualize the hierarchy of the files in your project.
3. Create a summary of all files.

*Using project reader from console*
-----------------------------------

This entails running project_reader module in console
``python -m project.read``. It takes one positional argument and two
other optional arguments. The positional argument is the path of the
project.

.. code:: bash

   python -m project.read "C:\Users\admin\django projects\blog-site"

Optional one is the folders to ignore in a comma-separated string.

.. code:: bash

   python -m project.read "C:\Users\admin\django projects\blog-site" --ignore ".idea, .vscode"

Optional two is the final output file.

.. code:: bash

   python -m project.read "C:\Users\admin\django projects\blog-site" --output "blog_site_tree.txt"

OR

.. code:: bash

   python -m project.read "C:\Users\admin\django projects\blog-site" --ignore ".idea, .vscode" --output "blog_site_tree.txt"

This will output a file a tree visualizing you project.

Go ahead and run the line below to learn more

.. code:: bash

   python -m project.read -h

*Using project reader in python code or from the interpreter*
-------------------------------------------------------------

You can choose to use from the interpreter or in your code using the
help of project.folder_reader.py and project.folder_visualizer.py


Folder visualizer (project.folder_visualizer.py)
------------------------------------------------

| Contains classes(Folder, File) and functions(assign_class,
  depth_calculator, draw) to help visualize the hierarchy.
| Example. This is **"test_FOLDER_GITHUB_PROJECTS_2.txt"** prepared by
  the function ``project.folder_reader.print_statement`` below.

Example 1


.. code:: text

   question_1.py - 38
   question_2(factorial).py - 66
   question_21.py - 45
   .IDEA
   github projects 2.iml - 11
   misc.xml - 5
   modules.xml - 9
   workspace.xml - 17
   DICTIONARIES
   muremwa.xml - 5
   ---- END OF DICTIONARIES ----
   ---- END OF .IDEA ----
   DESC

Run the code below

.. code:: python

   from project.folder_visualizer import assign_classes, draw


   klasses = assign_classes('test_FOLDER_GITHUB_PROJECTS_2.txt')
   draw(klasses, file_name="results.txt")

This is the output in "results.txt"

Example 2


.. code:: text

   GITHUB_PROJECTS_2
   |
   |---- question_1.py (38 lines)
   |
   |---- question_2(factorial).py (66 lines)
   |
   |---- question_21.py (45 lines)
   |
   |---- .IDEA
   |          |
   |          |---- github projects 2.iml (11 lines)
   |          |
   |          |---- misc.xml (5 lines)
   |          |
   |          |---- modules.xml (9 lines)
   |          |
   |          |---- workspace.xml (17 lines)
   |          |
   |          |---- DICTIONARIES
   |          |         |
   |          |         |---- muremwa.xml (5 lines)
   |
   |---- DESC


Folder reader (project.folder_reader.py)
----------------------------------------

Contains the following classes:

1. KillerFolder - extends the Folder class from
   project.folder_visualizer.py but adds the following methods (eq) and
   statement and the path property.
2. KillerFile - extends the File class from project.folder_visualizer.py
   but adds the path property
3. FolderStore - extends the in-built list class. It stores only
   KillerFolder objects.
4. RootDoesNotExist - an exception that is raised when one tries to
   access the root KillerFolder object of a FolderStore object that has
   none.

Contains the following functions:

1. kill_project - takes in a path of the folder to read, reads and
   returns a string representative of the files and folders similar to
   [example 1](#Example 1) above. You can add a keyword argument called
   ignore to show what folders to ignore.
2. print_statement - takes the statement from kill_project and writes it
   to a file and returns the name of that file. Usually
   FOLDER_SOMETHING.txt

Using project.folder_reader.py (demonstrated using the folder names TOP)

.. code:: python

   import os
   from project.folder_reader import kill_project, print_statement

   # change into the folder you want to read
   os.chdir(os.getcwd() + "\\TOP")

   # get the statement
   statement = kill_project(os.getcwd(), ignore=['.vscode', '.idea'])

   # write the statement to a file
   file_name = print_statement(statement)  # the file_name can be passes into folder_visualizer.assign_classes()

The last line writes to a file called "FOLDER_TOP.txt"

.. code:: text

   file.txt - 1
   VO
   s.txt - 1
   KO
   l1.txt - 1
   ---- END OF KO ----
   ---- END OF VO ----
   XO
   n.txt - 1
   BO
   temp.txt - 1
   ---- END OF BO ----
   JO
   sd.txt - 1
   PO
   l.txt - 1
   ---- END OF PO ----
   ---- END OF JO ----
   ---- END OF XO ----

Notice how the folder '.idea' was ignored.
