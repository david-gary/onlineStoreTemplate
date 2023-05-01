# Lab 3: Polygon Visualizer

## Introduction

The goal of this lab is to introduce you to module dependencies and inheritance in Python. This will require you to install a third-party module, Pygame, using the `pip` package manager. This lab is meant to be completed individually.

## Task 1: Installing Pygame with Pip

- Use pip to install the Pygame module. Shown below are a few variations of how the `pip` command may work on your machine. If the first doesn't work, move on to the next. If none of them work, ask for help.
  - `pip install pygame`
  - `py -m pip install pygame`
  - `python -m pip install pygame`
  - `python3 -m pip install pygame`
  - `python3.10 -m pip install pygame`
- Remember which command you used to install Pygame. This will be important for later tasks and future labs.

## Task 2: Completing the Polygons Class

- Open the `polygons.py` file.
- Complete `TODO 1` in the `Polygons` class by adding an attribute called `num_sides` and setting it equal to the parameter `num_sides` that is passed into the constructor.
- Complete `TODO 2` in the `Polygons` class by adding an attribute called `side_length` and setting it equal to the parameter `side_length` that is passed into the constructor.
- Complete `TODO 3` in the `Polygons` class by adding an attribute called `radius` and setting it equal to the result of the equation provided in the comments.
- Complete `TODO 4` in the `Polygons` class by adding an attribute called `area` and setting it equal to the result of the `polygon_area` method.

## Task 3: Fixing the Tkinter GUI

- Open the `tkinterGUI.py` file.
- Complete `TODO 5` in the `TkinterGUI` class by fixing the object's definition so that it inherits from the `Polygons` class.
- Complete `TODO 6` in the `TkinterGUI` class by fixing its constructor so that it calls the `Polygons` constructor and passes in the correct parameters. Use standard Python inheritance syntax to do this.

## Task 4: Fixing the Pygame GUI

- Open the `pygameGUI.py` file.
- Complete `TODO 7` in the `PygameGUI` class by fixing the object's definition so that it inherits from the `Polygons` class.
- Complete `TODO 8` in the `PygameGUI` class by fixing its constructor so that it calls the `Polygons` constructor and passes in the correct parameters. Use standard Python inheritance syntax to do this.

## Task 5: Installing More Packages

- Install all packages listed in the `requirements.txt` file using `pip`. You can do this by running a command like the following (may vary depending on which command worked for you in Task 1):
  - `pip install -r requirements.txt`
- Once you have successfully run the command above, run a command like the following to write the list of packages you have installed to a file called `pipFreeze.txt`:
  - `pip freeze > pipFreeze.txt`

## Submission Details

- On Canvas, submit the following:
  - A zip file of the entire `lab3` directory, renamed as your NinerNetID.zip (e.g., dgary9.zip)
    - **TIP:** If you are struggling to remember how to zip your submission, here's an example of how to do it from the terminal on Mac or Linux machines: `zip -r -X dgary9.zip .`
    - **TIP:** For Windows users who want to use their terminal to zip their submission, you can use the `7za` command. Here's an example of how to do it: `7za dgary9.zip .`
    - **NOTE:** In the above examples, `dgary9` is the NinerNetID of the student submitting the assignment and `.` is the directory that contains the files to be zipped, which is the current directory (`lab3`) in this case.
