# Lab 4: Git and Paired Programming

## Description

In this lab, you will practice basic git commands for a version control protected workflow. As a part of this, you will also work with a partner to simulate a common practice in software development: paired programming. The goal of this lab is to get you comfortable with essential version control commands, which will require you and your partner to carefully follow the instructions below.

## Task 1: Installing Git, Creating a GitHub Account, and Setting Up Keys

**THIS TASK IS HARD. PAY CLOSE ATTENTION TO THE INSTRUCTIONS AND WATCH THE VIDEOS CAREFULLY.**

- Install Git on your local machine.
  - **NOTE:** If you are on a Mac with Homebrew installed, you can run `brew install git` to install Git.
  - **NOTE:** If you are on a Mac without Homebrew installed, you can download the Git installer from [here](https://git-scm.com/download/mac).
  - **NOTE:** If you are on a Windows machine, you can download the Git installer from [here](https://git-scm.com/download/win).
- Create a GitHub account if you do not already have one.
  - **TIP:** DO NOT USE YOUR SCHOOL EMAIL ADDRESS. USE A PERSONAL EMAIL ADDRESS.
- Set up your SSH keys on your local machine.
  - **TIP:** Follow the official instructions on github [here](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh).
  - **TIP:** Watch the Git videos on Canvas for a demonstration of this process.
  - **TIP:** See the `gitGoing.md` document in this week's directory for more information on this process.
- Add your SSH key to your GitHub account.
  - **TIP:** Follow the official instructions on github [here](https://docs.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account).
  - **TIP:** Watch the Git videos on Canvas for a demonstration of this process.
  - **TIP:** See the `gitGoing.md` document in this week's directory for more information on this process.

## Task 2: Repository Setup via Forking and Cloning from GitHub

- One member from your pair should fork the [calculator repository](https://www.github.com/david-gary/CalculatorLab) to their GitHub account.
- Both members should clone the forked repository to their local machines.
  - **TIP:** Remember to run the `git clone` command from the parent directory of where you want the repository to be located.

## Task 3: Creating Separate Branches for Each Member

- First, make sure you are on the `main` branch of your local repository. You can check this by running `git branch`.
  - If you are, somehow, not on the `main` branch, you can switch to it by running `git checkout main`.
- Each member should create a new branch on their local machine (name it your first name) and push it to the forked repository.
  - **TIP:** Remember to push with the entire `git push -u origin <branch_name>` command (e.g., `git push -u origin main`)
  - **TIP:** If you are behind on your commits, you should pull the latest changes from the `main` branch before creating your new branch, and you may want to use the `-ff` flag when pulling.

## Task 4: Paired Programming Implementation

- Once you have created your branches, decide who will handle the `scientificOperations.py` file and who will handle the `simpleOperations.py` file.
- For each file, the person who is responsible for it should checkout their branch and finish the functions in the file while the other person watches, looks for errors, and provides feedback as needed.
- Once the functions are finished, the person who is responsible for the file should merge their branch into the `main` branch.
  - **TIP:** Remember to pull the latest changes from the `main` branch before merging your branch into it.
  - **TIP:** Remember to push the changes to the `main` branch after merging your branch into it.
  - **TIP:** And remember the basic process is `git add <file_name>`, `git commit -m "<commit_message>"`, `git pull -ff`, `git merge <branch_name>`, `git push -u origin main`.
- If a merge conflict occurs, the person who is responsible for the file should resolve the conflict and push the changes to the `main` branch.
  - **TIP:** See this [link](https://docs.github.com/en/github/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-using-the-command-line) for more information on how to resolve a merge conflict.
  - **TIP:** Or see this [link](https://www.youtube.com/watch?v=JtIX3HJKwfo) for a video demonstration of how to resolve a merge conflict.
  - **TIP:** If you are having trouble resolving a merge conflict, you can always delete the repository and start over, but that's not recommended.
- Together, finish both files and merge them into the `main` branch.

## Submission Details

- On Canvas, submit the following:
  - The URL to the finished `main` branch of your forked repository on GitHub.
