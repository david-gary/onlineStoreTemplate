# Lab 2: Types and Built-in Functions in Python

## Introduction

The goal of this lab is to provide some practice with types and some built-in functions in the Python language. Reading the commented documentation will help you greatly as you continue learning the basics of Python. This exercise requires students to work with a partner, so go be social!

## Task 1: Buddy Up

- Work in pairs with someone sitting near you.
- Both students participating in this lab must be enrolled in this class.
- Write down your student ID (or any 9 digit number) somewhere you can easily access it.
- You will each need to submit your own lab, so make sure you both complete the assignment on your own machine and submit it individually.

## Task 2: Converting Types and Using Built-in Functions

- Open the `hashStudentID.py` file.
- Complete `TODO 1` in the `key_from_student_ids` function by converting the student ID variables to integers.
- Complete `TODO 2` in the `key_from_student_ids` function by putting both student ID variables into a tuple named `hashed_tuple`. The function returns this tuple, so the variable name must be the same.
  - **TIP:** Official documentation for the built-in `hash()` function can be found [here](https://docs.python.org/3/library/functions.html#hash).
- Run the `hashStudentID.py` file and test that both main menu options work as expected. Tests are already written for you, just read the output and look for errors. If you see errors, fix them.

## Task 3: Mixed Types

- Open the `keyCollection.py` file and read through the code.
- Complete `TODO 3` inside the `add_student_id_record` method by properly adding the key/value pair to the `student_ids` attribute of the `StudentIDManager` class.
- Complete `TODO 4` inside the `calculate_all_keys` method by grabbing the first and last names for each student ID and concateninating them together with a single space in between.
- Complete `TODO 5` inside the `calculate_all_keys` method by calling the `key_from_student_ids` function from the `hashStudentID.py` file and storing it into the variable called `key`.
- Complete `TODO 6` inside the `calculate_all_keys` method by creating a list of `key`, `full_name_A`, and `full_name_B` in that order. Name the list `key_info`.
- Complete `TODO 7` inside the `calculate_all_keys` method by appending the `key_info` list to the `keys` list.

## Task 4: Using our Methods and Writing to a File

- Stay in the `keyCollection.py` file.
- Complete `TODO 8` inside the `main` function by calling the `add_student_id_record` method twice and passing in identifiable information for both you and your partner.
- Complete `TODO 9` inside the `main` function by calling the `write_all_ids_to_file` method and passing in the `keys.txt` file name.

## Submission Details

- On Canvas, submit the following:
  - A zip file of the entire lab2 directory, renamed as your NinerNetID.zip (e.g., dgary9.zip)
    - **TIP:** If you are struggling to remember how to zip your submission, here's an example of how to do it from the terminal: `zip -r -X dgary9.zip .`
      - **NOTE:** In the above example, `dgary9` is the NinerNetID of the student submitting the assignment and `.` is the directory that contains the files to be zipped, which is the current directory (`lab2`) in this case.
