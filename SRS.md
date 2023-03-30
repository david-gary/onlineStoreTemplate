# Software Requirements Specification Document

This serves as a template for each projects' Software Requirements Specification (SRS) document. When filling this out, you will be required to create user stories, use cases, requirements, and a glossary of terms relevant to your project. Each group member must contribute to every section, so it is crucial that your group's GitHub repository shows a commit history that reflects the work of each group member. It is highly recommended that you create separate branches for each member, but since this is one single document, you will need to manually merge the branches together. It is also advisable to have multiple working versions of this document (named separately) so that one person can compile the final SRS document from the multiple working versions. Ultimately, how you go about managing this is up to you, but consistent formatting, clear commit messages, and a thorough commit history with contributions from each group member are required.

Fill the document out following the guidelines listed in each section. Maintain [proper Markdown syntax](https://www.markdownguide.org/basic-syntax/) and be sure that your group has a `main` branch with this document and the entire [template repository codebase](https://github.com/david-gary/onlineStoreTemplate) either forked or downloaded and copied into your group's repository. If you have arranged to use a different codebase as a template, you do not need to have the original template included, but a `main` branch is still required.

## Group Members

* [Name](mailto:email@uncc.edu)
* [Name](mmailto:email@uncc.edu)
* [Name](mmailto:email@uncc.edu)
* [Mercere Baker](mmailto:mbaker89@uncc.edu)

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

* **ID:** REQ-10
  * **Description:** Needs to have a shopping cart feature to hold their item(s) to purchase.
 * **Type:** Functional
  * **Priority:** 5
  * **Rationale:** An online shopping cart is one of the foundations odf commerical websites to purchase products.
  * **Testing:** Trying to store items in the cart and then buying those items at checkout.

* **ID:** REQ-11
  * **Description:** Website needs to be clear to the clients.
  * **Type:** Non-functional
  * **Priority:** 2
  * **Rationale:** Though good design is not necessary "functional," it is important for clients to be able to use the website intuitively and have it make sense to them.
  * **Testing:** HTML elements need to work as expected and the website should be redesigned until clear.

* **ID:** REQ-12
  * **Description:** Checkout should only be available if there is at least one item in the shopping cart.
  * **Type:** Functional
  * **Priority:** 4
  * **Rationale:** Customers shouldn't be prompted to enter their card information if they're not about to buy anything.
  * **Testing:** When clicking on checkout, it should only proceed if there is an item in the cart.

## Constraints

In this section, you should list any constraints that you have for the project. Each group member must supply at least two constraints. These can be constraints on the project itself, the software system, or the stakeholders. Constraints can be anything that limits the scope of the project. For example, that this project's template code is written using Flask and Python constitutes a constraint on the backend of the project. Constraints can also be things like the required timeline of the project. Be creative.

Constraint 7: This project's code is written using Python, HTML, CSS, and Javascript.
Contstraint 8: The project has to be finished by the end of UNCC's 2023 spring semester.

## Use Cases

In this section, you should list use cases for the project. Use cases are a thorough description of how the system will be used. Each group member must supply at least two use cases. Each use case should be written in the following format:

* **ID:** UC-7
  * **Description:** The customer is virtual window shopping and is navigating around the website.
  * **Actors:** The customer
  * **Preconditions:** The customer can connect to the website
  * **Postconditions:** The customer should feel that navigation was simple and clear. The customer should not feel confused by going through our website.

* **ID:** UC-8
  * **Description:** The customer is trying to remove items from their shopping cart.
  * **Actors:** The customer
  * **Preconditions:** The customer can connect to the website, the shopping cart is functional, the customer has put items in the shopping cart.
  * **Postconditions:** The customer's shopping cart no longer has the item in the shopping cart. If the shopping cart only has that item, it should be empty and unable to proceed to checkout.

## User Stories

In this section, you should list user stories for the project. User stories are a short description of how a user will be interacting with the system. Each group member must supply at least two user stories. Each user story should be written in the following format

  * **ID:** US-7
    * **Type of User:** Customer
    * **Description:** The customer found our website and is interested in purchasing a piece of our jewelry. They browse the site, put an item in their shopping cart, click on the shopping cart icon, get taken to a checkout page, and confirm the order with an address and card information.
  * **ID:** US-8
    * **Type of User:** IT
    * **Description:** The customer has a question about the website or has problems purchasing their items. They can send their issues to the provided email to have it checked out.

## Glossary

In this section, you should list any terms that are used in the document that may not be immediately obvious to a naive reader. Each group member must supply at least one term. Each term should be written in the following format:

  * **Term:** shopping cart
    * **Definition:** software to allow customers to select products and buy them on the web.
