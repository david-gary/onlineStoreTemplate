# Lab 1: Basic Development Environment Setup

## Introduction

The purpose of this lab is to ensure you have a working development environment on your device and to introduce you to the Python programming language. This will require you to install Python and a working editor on your device. You will also be asked to write a Canvas discussion post in response to an article about software engineering.

### Preface

If you want to view these instructions in Google Chrome, we recommend installing this [Markdown Viewer Chrome Extension](https://chrome.google.com/webstore/detail/markdown-viewer/ckkdlimhmcjmikdlpkmbgfkaikojcbjk?hl=en).

## Task 1: Setup Your Integrated Development Environment

- Install an IDE on your device. This can be any general IDE, but we recommend [Visual Studio Code](https://code.visualstudio.com/).
  - If you are using Windows, you should also install the [Windows Terminal from the Microsoft Store](<https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab>) and [Windows Subsystem for Linux 2](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
  - If you are using Mac, you should also install [Homebrew](https://brew.sh/).
  - If you are using a Mac and do not know how to access your terminal, you can follow [these instructions](https://support.apple.com/guide/terminal/open-or-quit-terminal-apd5265185d-f365-44cb-8b09-71a064a42125/mac#:~:text=Terminal%20for%20me-,Open%20Terminal,%2C%20then%20double%2Dclick%20Terminal./).
- Make sure you know how to create files, access project directories, and run programs from the terminal.

## Task 2: Install and Run Python3.10.8 on Your Device

- For Windows users
  - Go to the [Python3.10.8 download page](https://www.python.org/downloads/release/python-3108/) and download the appropriate installer for your device (Windows).
  - Complete the installation of Python3.10.8 on your device, as prompted by the installer.
- For Mac users with Homebrew installed
  - Open a terminal and run the following command:
    - `brew install python3@3.10`
- For Mac users without Homebrew installed
  - Go to the [Python3.10.8 download page](https://www.python.org/downloads/release/python-3108/) and download the appropriate installer for your device (Mac).
  - Complete the installation of Python3.10.8 on your device, as prompted by the installer.
- For Linux users
  - Go to the [Python3.10.8 download page](https://www.python.org/downloads/release/python-3108/) and download the appropriate installer for your device (Linux).
  - Complete the installation of Python3.10.8 on your device, as prompted by the installer.
- Verify that Python3.10.8 is installed on your device by running the following command in a terminal:
  - `python3.10 --version`
  - If you see a version number that is not `3.10.8`, you may need to uninstall whatever version of Python you have installed and try again. Here's a walkthrough for [uninstalling Python](https://www.educative.io/answers/how-to-uninstall-python)
  - **TIP:** If you are using Windows, you may need to run `py -3.10 --version` instead.
  - **TIP:** If you are using Mac, you may need to run `python3 --version` instead.
- VS Code users are recommended to install the [VS Code Python Extensions](https://marketplace.visualstudio.com/items?itemName=ms-python.python).
- Finish the `helloWorld.py` file so that it prints `Hello, World!` to the terminal when run.
  - **TIP:** Make sure it prints `Hello, World!` and not `Hello, World`, `Hello World!`, `Hello World`, or any other variation. An error here will cause your submission to fail the autograder, and you will lose points.

## Task 3: The Curran Article Discussion Post

- This article can be found in module 1 of the course Canvas page or [at this link](https://ubiquity.acm.org/article.cfm?id=763745).
- Finish the discussion post assignment on Canvas for this week and paste your response into the file `response.txt` located in the `lab1` directory.

### Canvas Discussion

- Initial post due by Friday, 01/13/2023 at 11:59 PM.
- Minimum of 125 words; maximum of 500 words.
- Choose a field of study that is related to Software Engineering, and write a response (between 125 and 500 words) that answers the following questions:
  - What is the field of study? (e.g., Marketing, Management, IT, Psychology, etc.)
  - What is the relationship between the field of study and Software Engineering?
  - How does this field of study rank in terms of scientific rigor?
- Respond to at least two of your classmates' discussion posts by Sunday, 01/15/2023 at 11:59 PM.

## Task 4: IO in Python

- Inside the `responseReader.py` file, complete the `read_file` function so that it returns a string containing the contents a given file name (e.g., `response.txt`).
  - **TIP:** Section 7.2 of the [Python input/output documentation](https://docs.python.org/3.10/tutorial/inputoutput.html) may be helpful.
- Run the `responseReader.py` file to see if your response meets the length requirements.

## Submission Details

- On Canvas, submit the following:
  - A zip file of the entire lab1 directory, renamed as your NinerNetID.zip (e.g., dgary9.zip)
    - **TIP:** If you are struggling to remember how to zip your submission, here's an example of how to do it from the terminal: `zip -r -X dgary9.zip .`
      - **NOTE:** In the above example, `dgary9` is the NinerNetID of the student submitting the assignment and `.` is the directory that contains the files to be zipped, which is the current directory (`lab1`) in this case.
