# Software Requirements Specification Document

This serves as a template for each projects' Software Requirements Specification (SRS) document. When filling this out, you will be required to create user stories, use cases, requirements, and a glossary of terms relevant to your project. Each group member must contribute to every section, so it is crucial that your group's GitHub repository shows a commit history that reflects the work of each group member. It is highly recommended that you create separate branches for each member, but since this is one single document, you will need to manually merge the branches together. It is also advisable to have multiple working versions of this document (named separately) so that one person can compile the final SRS document from the multiple working versions. Ultimately, how you go about managing this is up to you, but consistent formatting, clear commit messages, and a thorough commit history with contributions from each group member are required.

Fill the document out following the guidelines listed in each section. Maintain [proper Markdown syntax](https://www.markdownguide.org/basic-syntax/) and be sure that your group has a `main` branch with this document and the entire [template repository codebase](https://github.com/david-gary/onlineStoreTemplate) either forked or downloaded and copied into your group's repository. If you have arranged to use a different codebase as a template, you do not need to have the original template included, but a `main` branch is still required.

## Group Members

* [Name](mailto:email@uncc.edu)
* [Akanimoh Joseph Umoren](mmailto:aumoren@uncc.edu)
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

In this section, you should give a brief overview of what your project will be. Describe the software system you are building and what problems it solves. You should also give a short description of the stakeholders (users of the system) and what their needs are. There is no set formatting requirement, but you should maintain a consistent structure across future sections. Not all members must contribute to this section.

## Requirements

Each group member must supply at least three functional requirements for the project. Each requirement should be written in the following format:


* **ID:** REQ-4
  * **Description:** Website should ask the user to confirm their purchase before charging them.
  * **Type:** Functional
  * **Priority:** 2
  * **Rationale:** This is important so that the user does not accidentaly purchase items they do not mean to
  * **Testing:** Trying to checkout the items in a cart, the user shoukld be prompted to confirm that the items are correct.

* **ID:** REQ-5
  * **Description:** Wesite should have a navigation bar which displays the main types of items being sold
  * **Type:** Functional
  * **Priority:** 3
  * **Rationale:** This is important because it helps the user navigate the website easily.
  * **Testing:** The webpage sould dsplay a visible navigation bar that can be used to go through the ite,s in the website easiy.

* **ID:** REQ-6
  * **Description:** Upon payment, a confirmation of purchase should be displayed to the user
  * **Type:** Functional
  * **Priority:** 2
  * **Rationale:** This is important because it lets the user know that their purchase was successful.
  * **Testing:** When the user pays for the items, they should be redirected to another page which displays a confirmation message and the details of their purchase like purchase id, shipping addresss, and delivery date.

## Constraints

In this section, you should list any constraints that you have for the project. Each group member must supply at least two constraints. These can be constraints on the project itself, the software system, or the stakeholders. Constraints can be anything that limits the scope of the project. For example, that this project's template code is written using Flask and Python constitutes a constraint on the backend of the project. Constraints can also be things like the required timeline of the project. Be creative.




Constraint 3: We do not display stakeholder reviews but we have admin reviews.
Constraint 4: We do not control delivery prices because we deliver products using a third party delivery system.





## Use Cases

In this section, you should list use cases for the project. Use cases are a thorough description of how the system will be used. Each group member must supply at least two use cases. Each use case should be written in the following format:

* **ID:** UC-3
  * **Description:** The customer clicks the checkout button
  * **Actors:** The customer
  * **Preconditions:** The customer has at least one item in their cart
  * **Postconditions:** The items in the customer's cart are displayed and they are prompted to confirm that akll the items and their amounts are correct.

* **ID:** UC-4
  * **Description:** The customer completes their purchase
  * **Actors:** The customer
  * **Preconditions:** The customer went through all the necessary purchase steps without any issues
  * **Postconditions:** The customer is redirected to a page where a confirmation message of their order is displayed and other information about the details of th purchase is displayed as well.

## User Stories

In this section, you should list user stories for the project. User stories are a short description of how a user will be interacting with the system. Each group member must supply at least two user stories. Each user story should be written in the following format:

* **ID:** US-3
  * **Type of User:** Customer
  * **Description:** The customer does not want to delete an item in cart that they do not want to purchase anymore. They click on the cart icon which lists the items in their cart and there is an option to remove each item from the cart. They successfully remove the item they do not need anymore.

* **ID:** US-4
  * **Type of User:** Customer
  * **Description:** The customer is currently viewing necklaces and wants to look at rings instead. They use the navigation bar to successfully got to the ring section.

In this section, you should list any terms that are used in the document that may not be immediately obvious to a naive reader. Each group member must supply at least one term. Each term should be written in the following format:

* **Term:** Navigation bar
  * **Definition:** The webpage element that helps users navigate through the use of hyperlinks.