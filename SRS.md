# Software Requirements Specification Document

This serves as a template for each projects' Software Requirements Specification (SRS) document. When filling this out, you will be required to create user stories, use cases, requirements, and a glossary of terms relevant to your project. Each group member must contribute to every section, so it is crucial that your group's GitHub repository shows a commit history that reflects the work of each group member. It is highly recommended that you create separate branches for each member, but since this is one single document, you will need to manually merge the branches together. It is also advisable to have multiple working versions of this document (named separately) so that one person can compile the final SRS document from the multiple working versions. Ultimately, how you go about managing this is up to you, but consistent formatting, clear commit messages, and a thorough commit history with contributions from each group member are required.

Fill the document out following the guidelines listed in each section. Maintain [proper Markdown syntax](https://www.markdownguide.org/basic-syntax/) and be sure that your group has a `main` branch with this document and the entire [template repository codebase](https://github.com/david-gary/onlineStoreTemplate) either forked or downloaded and copied into your group's repository. If you have arranged to use a different codebase as a template, you do not need to have the original template included, but a `main` branch is still required.

## Group Members

* [Beren Hollingsworth](mailto:bhollin8@uncc.edu)
* [Matthew Murphy](mmailto:mmurph83@uncc.edu)
* [Fernando Contreras-Juarez](mailto:fcontre1@uncc.edu)
* [Name](mmailto:email@uncc.edu)

## Revisions

When a change is made to the document, a new revision should be created. The revision should be added to the table below with all information filled out.

| Version | Date | Description | Author | Reviewed By |
| --- | --- | --- | --- | --- |
| 1.0 | 03/22/23 | Initial draft | [David Gary](mailto:dgary9@uncc.edu) | [David Gary](mailto:dgary@uncc.edu) |
| 1.1 | 03/30/23 | Adding introduction theme | [Beren Hollingsworth](mailto:bhollin8@uncc.edu) | [Beren Hollingsworth](mailto:bhollin8@uncc.edu) |
| 1.2 | 03/30/23 | Adding simple requirements | [Beren Hollingsworth](mailto:bhollin8@uncc.edu) | [Beren Hollingsworth](mailto:bhollin8@uncc.edu) |

## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Constraints](#constraints)
4. [Use Cases](#use-cases)
5. [User Stories](#user-stories)
6. [Glossary](#glossary)

## Introduction

CodeCompanionSE is a resource website for the ITSC 3155 Software Engineering class. This resource seeks to provide `Student`s information relating to their completion of the ITSC 3155 lab assignments. The website will show information on each lab and lab topic as well as displaying requirements, files, related documentation, and examples of lab related material. This page should assist the `Student`s in succeeding throughout the labs.

## Requirements

Each group member must supply at least three functional requirements for the project. Each requirement should be written in the following format:

* **ID:** A unique identifier for the requirement. This should be a number that is unique across the entire document (something like REQ-1, REQ-2, etc. but be sure to replace the word `ID` with the unique identifier).
  * **Description:** A short description of the requirement. This should be a single sentence that describes the requirement. Do not replace the word `Description` with the actual description. Put the description in the space where these instructions are written. Maintain that practice for all future sections.
  * **Type:** The type of requirement. Should be either `Functional` or `Non-Functional`.
  * **Priority:** The priority of the requirement. This should be a number between 1 and 5, with 1 being the highest priority and 5 being the lowest priority.
  * **Rationale:** A short description of why the requirement is important. This should be a single sentence that describes why the requirement is important.
  * **Testing:** A short description of how the requirement can be tested. This should be a single sentence that describes how the requirement can be tested.

* **REQ-0:**
  * **Description:** Website displays tiles with each tile representing one ITSC 3155 lab.
  * **Type:** `Functional`
  * **Priority:** 5
  * **Rationale:** Displaying labs and lab information is the critical foundation for the functionality of the website. The site should be able to show all the labs related to the class in a viewable manner.
  * **Testing:** All labs for the class should be visible within a minimal amount of scrolling from the homepage of the website. Each lab should look unique and be easily discernable. 
* **REQ-1:**
  * **Description:** Lab tiles are clickable and take the user to more detailed information on the lab.
  * **Type:** `Functional`
  * **Priority:** 5
  * **Rationale:** This functionality allows us to show much more detailed information as well as offering screen space for download buttons and resource links.
  * **Testing:** All lab tiles should be able to be clicked to take the user to a separate web page for each lab.
* **REQ-2:**
  * **Description:** Lab informational markdown files are displayed in webpage. 
  * **Type:** `Functional`
  * **Priority:** 3
  * **Rationale:** Being able to show the lab README or other instructional markdown file will give `Student`s an easy way to view their intructions for each lab.
  * **Testing:** Markdown files for each lab are visible on the lab webpage.
* **REQ-3:**
  * **Description:** Have A .ZIP file of the lab available to download.
  * **Type:** `Functional`
  * **Priority:** 1
  * **Rationale:** Have the `Student`s easily able to work and edit their version of the lab without having to use an external resource.
  * **Testing:** All lab files should be able to be downloaded.
* **REQ-4**
  * **Description:** `Student` requires user login to access labs.
  * **Type:** `Functional`
  * **Priority:** 3
  * **Rationale:** `Student` can keep track of labs that have been accessed.
  * **Testing:** Labs should be accessible to those who are logged in.
* **REQ-5**
  * **Desciption:** Website able to handle 50 concurrent users logged in.
  * **Type:** `Non Functional`
  * **Priority:** 3
  * **Rationale:** The Website can handle the traffic if `Student`s are seeking to log on.
  * **Testing:** This allows almost the entire class to be logged in and accessing labs.



## Constraints

In this section, you should list any constraints that you have for the project. Each group member must supply at least two constraints. These can be constraints on the project itself, the software system, or the stakeholders. Constraints can be anything that limits the scope of the project. For example, that this project's template code is written using Flask and Python constitutes a constraint on the backend of the project. Constraints can also be things like the required timeline of the project. Be creative.

* **CON-0:**
  * The database should store course material progression so that it is instanced for each unique user.
* **CON-1:**
  * The logic of the website will be written in Python with Flask.

## Use Cases

In this section, you should list use cases for the project. Use cases are a thorough description of how the system will be used. Each group member must supply at least two use cases. Each use case should be written in the following format:

* **ID:** A unique identifier for the use case. This should be a number that is unique across the entire document (something like UC-1, UC-2, etc. but be sure to replace the word `ID` with the unique identifier).
  * **Description:** A description of the use case that gives the user a high-level overview of how the system is interacted with.
  * **Actors:** A list of the actors that are involved in the use case. Only include the actors that are directly involved. Actors are the people or things that interact with the system. For example, when ordering at a fast food restaurant, one might have the following actors: the customer, the cashier, and the cook. But only the customer and the cashier are directly involved in the use case of ordering food. The cook is not directly involved in the use case of ordering food.
  * **Preconditions:** A list of the preconditions for the use case. This should be a list of the preconditions for the use case, which are the conditions that must be met before the use case can be executed. Continuing with the restaurant example, the customer must have money in their wallet and the cashier must be logged in to the system before the use case of ordering food can be executed.
  * **Postconditions:** A list of the postconditions for the use case. This should be a list of the postconditions for the use case, which are the conditions that must be met after the use case has been executed. Continuing with the restaurant example, the customer must have their food and the cashier must have the customer's money after the use case of ordering food has been executed.

* **UC-0:**
  * **Description:** A `Student` checks the website to see when labs are due.
  * **Actors:** `Student`
  * **Preconditions:** The `Student` must be logged in and the instructor must have set the due date for the lab.
  * **Postconditions:** The `Student` must understand when the labs are due.
* **UC-1:**
  * **Description:** A `Student` reads instructions for the lab.
  * **Actors:** `Student`
  * **Preconditions:** The `Student` must be logged in and the markdown instructions must have been made available on the website.
  * **Postconditions:** The `Student` is able to read the markdown file and understand what is required from the lab.
* **UC-2:**
  * **Description:** A `Student` downloads the lab files from the website.
  * **Actors:** `Student`
  * **Preconditions:** The `Student` must be logged in and the lab files must have been uploaded to the website.
  * **Postconditions:** The `Student` has downloaded all files relating to the lab.

## User Stories

In this section, you should list user stories for the project. User stories are a short description of how a user will be interacting with the system. Each group member must supply at least two user stories. Each user story should be written in the following format:

* **ID:** A unique identifier for the user story. This should be a number that is unique across the entire document (something like US-1, US-2, etc. but be sure to replace the word `ID` with the unique identifier).
  * **Type of User:** The type of user that the user story is for. This should be a single word that describes the type of user. For example, a user story for a customer might be `Customer` and a user story for an administrator might be `Admin`.
  * **Description:** A description of the user story that gives a narrative from that user's perspective. This can be any length, but it must paint the picture of what the user wants to do, how they intend to do it, why they want to, and what they expect to happen.

* **US-0:**
  * **Type of User:** `Student`
  * **Description:** A `Student` realises that they totally forgot about a lab that they think might be due soon. The `Student` opens the website to check the due date. The `Student` signs on to the page and views the most current assignment that they have not yet completed. The `Student` compares the due date to the current time and determines how much they need to panic.
* **US-1:**
  * **Type of User:** `Student`
  * **Description:** A `Student` is in a large state of panic because a lab is due very soon. The `Student` is able to quickly download the completed lab files from the website. The website provides documentation links and examples to help the `Student` understand what they are expected to do. The `Student` is able to efficiently complete the lab given the resources. 

## Glossary

In this section, you should list any terms that are used in the document that may not be immediately obvious to a naive reader. Each group member must supply at least one term. Each term should be written in the following format:

* **Lab:**
  * **Definition:** An assignment from the ITSC 3155 Software Engineering class.
