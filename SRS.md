# Software Requirements Specification Document

This serves as a template for each projects' Software Requirements Specification (SRS) document. When filling this out, you will be required to create user stories, use cases, requirements, and a glossary of terms relevant to your project. Each group member must contribute to every section, so it is crucial that your group's GitHub repository shows a commit history that reflects the work of each group member. It is highly recommended that you create separate branches for each member, but since this is one single document, you will need to manually merge the branches together. It is also advisable to have multiple working versions of this document (named separately) so that one person can compile the final SRS document from the multiple working versions. Ultimately, how you go about managing this is up to you, but consistent formatting, clear commit messages, and a thorough commit history with contributions from each group member are required.

Fill the document out following the guidelines listed in each section. Maintain [proper Markdown syntax](https://www.markdownguide.org/basic-syntax/) and be sure that your group has a `main` branch with this document and the entire [template repository codebase](https://github.com/david-gary/onlineStoreTemplate) either forked or downloaded and copied into your group's repository. If you have arranged to use a different codebase as a template, you do not need to have the original template included, but a `main` branch is still required.

## Group Members

* [Sreyas Kodukulla](mmailto:skodukul@uncc.edu)
* [Name](mmailto:email@uncc.edu)
* [Name](mmailto:email@uncc.edu)
* [Name](mmailto:email@uncc.edu)

## Revisions

When a change is made to the document, a new revision should be created. The revision should be added to the table below with all information filled out.

| Version | Date | Description | Author | Reviewed By |
| --- | --- | --- | --- | --- |
| 1.0 | 03/22/23 | Initial draft | [David Gary](mailto:dgary9@uncc.edu) | [David Gary](mailto:dgary@uncc.edu) |

## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Constraints](#constraints)
4. [Use Cases](#use-cases)
5. [User Stories](#user-stories)
6. [Glossary](#glossary)

## Introduction

The idea for our project is to create a hands on jewlery store. We will build a system that has features to be able to search for jewlery based on the type and the material. The software system will allow users to perform filtered searches, create a wishlist or shopping cart for any items, and it will also display every item and give a brief description of it. Our stakeholders are the individual customers that are interested in buying products from our store. Their needs are the products we offer and we will give them the ability to browse through to find the right item to fit their needs.


## Requirements

Each group member must supply at least three functional requirements for the project. Each requirement should be written in the following format:

  * **ID:** REQ-1
    * **Description:** The customer is trying to use the filter search funtion to find the right type of chain.
    * **Type:** Functional
    * **Priority:** 4
    * **Rationale:** This is important because it will test a key feature of our store.
    * **Testing:** We can test the requirement by seeing if the 'filter search' function returns the correct output after the user input.

  * **ID:** REQ-2
    * **Description:** The items will have a small description to help the users with their selections.
    * **Type:** non-functional
    * **Priority:** 3
    * **Rationale:** This is important because it makes the store easier to navigate.
    * **Testing:** We will test this by seeing if the description shows once we finish the webpage.

  * **ID:** REQ-3
    * **Description:** The webiste needs to flow properly in the sense that the user should be able to follow the right path based on how they interact. Must have clear and consise UI.
    * **Type:** functional
    * **Priority:** 5
    * **Rationale:** This is important because if the user clicks to view chains, but rings show up instead, that means the webpage isn't up to the standards we want it to be at.
    * **Testing:** We will test this by using the website after completeion and test the flow based on user input.

## Constraints

In this section, you should list any constraints that you have for the project. Each group member must supply at least two constraints. These can be constraints on the project itself, the software system, or the stakeholders. Constraints can be anything that limits the scope of the project. For example, that this project's template code is written using Flask and Python constitutes a constraint on the backend of the project. Constraints can also be things like the required timeline of the project. Be creative.

Constraint 1: We cannot include recommended items because we can't collect the user data to narrow it down.
Constraint 2: Stakeholders cannot choose from a very vast collection of items, our site will be limited to only the scope of items we can include. 

## Use Cases

In this section, you should list use cases for the project. Use cases are a thorough description of how the system will be used. Each group member must supply at least two use cases. Each use case should be written in the following format:

  * **ID:** UC-1
    * **Description:** The customer is trying to utilize the filter search funtion.
    * **Actors:** The customer
    * **Preconditions:** There needs to be an option for filter search that is clear and easy to find.
    * **Postconditions:** The search must come up with the proper result based on the filters that the customer applies.

  * **ID:** UC-2
    * **Description:** The customer should be able to properly view and read about every item we offer.
    * **Actors:** The customer
    * **Preconditions:** The items must be displayed in a neat and visually pleasing manner while also having the proper descriptions.
    * **Postconditions:** Once the customer navigates to their desired item, they must be able to see the exact item they searched for with an image and description.

## User Stories

In this section, you should list user stories for the project. User stories are a short description of how a user will be interacting with the system. Each group member must supply at least two user stories. Each user story should be written in the following format:

* **ID:** A unique identifier for the user story. This should be a number that is unique across the entire document (something like US-1, US-2, etc. but be sure to replace the word `ID` with the unique identifier).
  * **Type of User:** The type of user that the user story is for. This should be a single word that describes the type of user. For example, a user story for a customer might be `Customer` and a user story for an administrator might be `Admin`.
  * **Description:** A description of the user story that gives a narrative from that user's perspective. This can be any length, but it must paint the picture of what the user wants to do, how they intend to do it, why they want to, and what they expect to happen.

  * **ID:** US-1
    * **Type of User:** Customer
    * **Description:** The customer opens up the website, navigates to the filter search button because they are looking for a certain type of ring, they apply the filters, and they will be directed to the options we offer based on their preference.

  * **ID:** US-2
    * **Type of User:** Customer
    * **Description:** The user navigates to the item they desire. Once they do that, they click on the image of the item and are shown a brief description about what the item is to aid them with their shopping experience.

## Glossary

In this section, you should list any terms that are used in the document that may not be immediately obvious to a naive reader. Each group member must supply at least one term. Each term should be written in the following format:

* **Term:** Filter Search
  * **Definition:** the filter search is when a user can input certain things that they are looking for and not looking for (based on price, material, type) and will find items that match the conditions they have set in the search.
