# Lab 8: Data Formats and Flow

## Introduction

In this lab you will practice your scraping skills and learn how to store scraped data in two different formats: JSON files and SQLite databases. This will require you to use methods from the [selenium](https://selenium-python.readthedocs.io/index.html), [json](https://docs.python.org/3/library/json.html), and [sqlite3](https://docs.python.org/3/library/sqlite3.html) libraries in Python. From there, you will use the data to create a simple web application that displays the scraped data in a readable format. The goal of this lab is to get a feel for how we can manipulate the flow of data from external sources into a workable format for our own software systems.

## Task 1: Accessing the ChromeDriver Again

- Complete `TODO 1` by either copying your chromedriver from the previous lab or by downloading it again from the [ChromeDriver website](https://chromedriver.chromium.org/downloads). Either place the chromedriver in the `chromedriver` folder of this lab.

## Task 2: Scraping Practice

- Open the `scrape_jobs.py` file.
- Complete `TODO 2` by creating a new driver instance with the correct path to the chromedriver and having it get the correct URL.
- Complete `TODO 3` by grabbing all elements with the given class name and storing them into the `job_elements` variable.
- Complete `TODO 4` by implementing the code to grab the values requested in the comments.
  - **TIP**: If you are unfamiliar with `try`/`except` blocks, check out the [documentation](https://docs.python.org/3/tutorial/errors.html#handling-exceptions) for details on how to use them.
  - **NOTE**: DO NOT CHANGE THE DICTIONARY KEY NAMES. USE WHAT IS LISTED.
- Complete `TODO 5` by appending the `job` dictionary to the `jobs` list.
- Run the `scrape_jobs.py` file.
  
## Task 5: Parsing to JSON

- Open the `json_writer.py` file.
- Complete `TODO 6` by implementing the code to convert the `dict_list` to a JSON string.
  - **HINT**: There are dozens of ways to do this, but the easiest way can be found [here](https://docs.python.org/3/library/json.html#basic-usage).

## Task 6: Storing and Querying Data in SQLite

- Open the `run_database.py` file.
- Complete `TODO 7` by creating a new JobsDatabase object and saving it to the `jobs_database` variable.
- Complete `TODO 8` by creating the `jobs` table in the database.
- Complete `TODO 9` by clearing out the `jobs` table in the database.
- Complete `TODO 10` by inserting the values from the `jobs` list into the `jobs` table.
- Complete `TODO 11` by pulling all jobs from the `jobs` table and printing them out.

## Task 7: Using the Data

- Open the `app.py` file.
- Complete `TODO 12` by finishing the `jobs` route function so that it loads the `jobs` list from the `jobs.json` file and returns it as a JSON string.
- Open the `templates/index.html` file.
- Complete `TODO 13` by making flask dynamically load the `title` for the current job.
- Complete `TODO 14` by making flask dynamically load the `company` for the current job.
- Complete `TODO 15` by making flask dynamically load the `image_url` for the current job.
  - **NOTE**: The `image_url` is a relative path to the `static` folder. See the stylesheet link at the top of the file for more information.

## Submission Details

- On Canvas, submit the following:
  - A zip file of the entire `lab8` directory, renamed as your NinerNetID.zip (e.g., dgary9.zip)
    - **TIP:** If you are struggling to remember how to zip your submission, here's an example of how to do it from the terminal on Mac or Linux machines: `zip -r -X dgary9.zip .`
    - **TIP:** For Windows users who want to use their terminal to zip their submission, you can use the `7za` command. Here's an example of how to do it: `7za dgary9.zip .`
    - **NOTE:** In the above examples, `dgary9` is the NinerNetID of the student submitting the assignment and `.` is the directory that contains the files to be zipped, which is the current directory (`lab8`) in this case.
