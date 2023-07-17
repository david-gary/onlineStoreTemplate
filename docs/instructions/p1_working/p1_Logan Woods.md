# Project 1: Software Requirements Specification Document

This serves as a template for each projects' Software Requirements Specification (SRS) document. When filling this out, you will be required to create user stories, use cases, requirements, and a glossary of terms relevant to your project. Each group member must contribute to every section, so it is crucial that your group's GitHub repository shows a commit history that reflects the work of each group member. It is highly recommended that you create separate branches for each member, but since this is one single document, you will need to manually merge the branches together. It is also advisable to have multiple working versions of this document (named separately) so that one person can compile the final SRS document from the multiple working versions. Ultimately, how you go about managing this is up to you, but consistent formatting, clear commit messages, and a thorough commit history with contributions from each group member are required.

Fill the document out following the guidelines listed in each section. Maintain [proper Markdown syntax](https://www.markdownguide.org/basic-syntax/).

## Group Members

- [Logan Woods](mailto:lwoods14@uncc.edu)
- [Kyle Davis](mailto:kdavi224@uncc.edu)
- [Elijah Robinson](mailto:erobin34@uncc.edu)

## Revisions

When a change is made to the document, a new revision should be created. The revision should be added to the table below with all information filled out.

| Version | Date | Description | Author | Reviewed By |
| --- | --- | --- | --- | --- |
| 1.0 | 03/22/23 | Initial draft | [David Gary](mailto:dgary9@uncc.edu) | [David Gary](mailto:dgary@uncc.edu) |
|1.1 | 07/16/23 | lwoods14 contents added | [Logan Woods](mailto:lwoods14@uncc.edu) | [None]

## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Constraints](#constraints)
4. [Use Cases](#use-cases)
5. [User Stories](#user-stories)
6. [Glossary](#glossary)

## Introduction

For this group project, we will be developing and implementing an online cafe that meets the functional and non-functional requirements outlined in the following sections. Our shareholders will primarily be members of the under-thirty crowd who are comfortable with technology and e-commerce.

## Requirements

Each group member must supply at least three functional requirements for the project. Each requirement should be written in the following format:

- **ID:** REQ-1
  - **Description:** The web application will have a secure and smooth login functionality.
  - **Type:** Functional
  - **Priority:** 2
  - **Rationale:** Login and logout functionality allows users to have the product securely accessed without outside interference.
  - **Testing:** Automated tests can be used to ensure that users can successfully login and logout.
- **ID:** REQ-2
  - **Description:** The application will successfully utilize a SQL database to store product information.
  - **Type:** Functional
  - **Priority:** 4
  - **Rationale:** SQL databases are an efficient way to store information about numerous and diverse products.
  - **Testing:** The database can be tested by inserting and deleting items, as well as testing edge cases.

## Constraints

- **Constraint:** There is a limited amount of computational power available, so computationally intensive actions will not be available.
- **Constraint:** The platform will be constrained to a web applicaition, multi-platform functionality is not possible.

## Use Cases

In this section, you should list use cases for the project. Use cases are a thorough description of how the system will be used. Each group member must supply at least two use cases. Each use case should be written in the following format:

- **ID:** UC-1
  - **Description:** An administrator logging in to modify the price for a product.
  - **Actors:** An administrator.
  - **Preconditions:** The administrator must posess an account with admin privilages on the web server.
  - **Postconditions:** The admin must be able to modify the product data stored in a SQL database.
  - **ID:** UC-2
    - **Description:** A user ordering a product from the web application.
    - **Actors:** A logged-in user.
    - **Preconditions:** The user must possess the necessary amount of money in their account, and the user must posess a valid account.
    - **Postconditions:** The user should receive a notification confirming that their purchase was a success.

## User Stories

In this section, you should list user stories for the project. User stories are a short description of how a user will be interacting with the system. Each group member must supply at least two user stories. Each user story should be written in the following format:

- **ID:** US-1
  - **Type of User:** New Customer
  - **Description:** The user is a customer who has not yet created an account. They proceed to register using their name, email address, and password. After registering, they are able to log into their account for all future sessions.
  - **ID:** US-2
    - **Type of User:** Terminating Customer
    - **Description:** The user is a customer who wishes to delete their account and all data associated with it. The user clicks the "Delete Account" button and is asked to confirm their choice. After confirming, their account is securely terminated.

## Glossary

In this section, you should list any terms that are used in the document that may not be immediately obvious to a naive reader. Each group member must supply at least one term. Each term should be written in the following format:

- **Term:** Administrator/Admin
  - **Definition:** A maintainer of a system with privelages higher than what is reserved for a typical user.

Try to only list terms that a naive user would not understand.

## Submission Details

- On Canvas, submit the following:
  - The URL to your group's GitHub repository, with the latest version of your code pushed to the `main` branch.
