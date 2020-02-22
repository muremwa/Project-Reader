# Project Reader
An easy way to count the number of lines in your project. (To be added) 
There is also and easy function to draw the hierarchy of your projects.

## Folder visualizer 
Contains classes(Folder, File) and functions(assign_class, depth_calculator, draw) to help visualize the hierarchy.  
Example. This is ___"test_FOLDER_GITHUB_PROJECTS_2.txt"___ prepared by a function __"coming soon"__.  

```txt
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
```
Run the code below
```python
from folder_visualizer import assign_classes, draw


klasses = assign_classes('test_FOLDER_GITHUB_PROJECTS_2.txt')
draw(klasses, file_name="results.txt")

```
This is the output in "results.txt"
```txt
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
|                    |
|                    |---- muremwa.xml (5 lines)
|
|---- DESC

```

__THIS IS AN ONGOING PROJECT__