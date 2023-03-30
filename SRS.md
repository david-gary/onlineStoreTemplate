# Software Requirements Specification Document

This serves as a template for each projects' Software Requirements Specification (SRS) document. When filling this out, you will be required to create user stories, use cases, requirements, and a glossary of terms relevant to your project. Each group member must contribute to every section, so it is crucial that your group's GitHub repository shows a commit history that reflects the work of each group member. It is highly recommended that you create separate branches for each member, but since this is one single document, you will need to manually merge the branches together. It is also advisable to have multiple working versions of this document (named separately) so that one person can compile the final SRS document from the multiple working versions. Ultimately, how you go about managing this is up to you, but consistent formatting, clear commit messages, and a thorough commit history with contributions from each group member are required.

Fill the document out following the guidelines listed in each section. Maintain [proper Markdown syntax](https://www.markdownguide.org/basic-syntax/) and be sure that your group has a `main` branch with this document and the entire [template repository codebase](https://github.com/david-gary/onlineStoreTemplate) either forked or downloaded and copied into your group's repository. If you have arranged to use a different codebase as a template, you do not need to have the original template included, but a `main` branch is still required.

## Group Members

* [Name](mailto:email@uncc.edu)
* [Name](mmailto:email@uncc.edu)
* [Blaise Thomas](mmailto:bthom108@uncc.edu)
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

* **ID:** REQ-7
  * **Description:** Different Page per product
  * **Type:** Functional
  * **Priority:** 1
  * **Rationale:** You'd have a list of the different products with images, onclick it will take you to just the 
  the Item itself
  * **Testing:** Onclick should take you to different webPages
* **ID:** REQ-8
  * **Description:** FAQ PAGE
  * **Type:** Non-Functional, gives people answers to FAQs
  * **Priority:** 5
  * **Rationale:** When people have similar questions and need quick answers a FAQ page is usually what they'll seek out. 
  * **Testing:** Test page on click
  * **ID:** REQ-9
  * **Description:** Works on Mobile
  * **Type:** Functional
  * **Priority:** 3
  * **Rationale:** Makes sure the Users have the same experience across all platforms
  * **Testing:** Can test by adjusting window size

## Constraints

In this section, you should list any constraints that you have for the project. Each group member must supply at least two constraints. These can be constraints on the project itself, the software system, or the stakeholders. Constraints can be anything that limits the scope of the project. For example, that this project's template code is written using Flask and Python constitutes a constraint on the backend of the project. Constraints can also be things like the required timeline of the project. Be creative.


Constraint 4: No automated payments accepted, Only Debit/Credit Cards. Only Available to US Region

## Use Cases

In this section, you should list use cases for the project. Use cases are a thorough description of how the system will be used. Each group member must supply at least two use cases. Each use case should be written in the following format:

* **ID:** UC-5
  * **Description:** Making a singular webpage for each item with more depth of review and descriptions that also allows them to add to cart
  * **Actors:** I will be building the web page, and adding the extra descriptions, Mercer will be going behind me to make sure the webpage will link to the checkout page
  * **Preconditions:** Has to come from a previous page that was the items brief description, I.E Under the rings page it is the ring 3 Item, clicking that leads to the ring 3 Item webpage
  * **Postconditions:** You've landed on the webpage for that specific item, complete with the photo, description, and add to cart button. 
  **ID:** UC-6
  * **Description:** Making sure that the webpages works across all devices
  * **Actors:** I will be making sure that the customers can access the page from different devices, such as tablets, smartphones, and computers
  * **Preconditions:** Has a device that can display webpage
  * **Postconditions:** The webpage displays properly with no errors or loss in usability
## User Stories

In this section, you should list user stories for the project. User stories are a short description of how a user will be interacting with the system. Each group member must supply at least two user stories. Each user story should be written in the following format:

* **ID:** US-5 Web page that displays the item, a description, and an add to cart button for the user to purchase. 
  * **Type of User:** Customer
  * **Description:** As I'm looking through the catalouge I noticed an item that I liked, I clicked on the item and it took me to a separate page that provided more detail for me to make an informed decision, I then added to cart and return to shopping.
* **ID:** US-6 Web page that displays properly regardless of the device used to acess it.
  * **Type of User:** Customer
  * **Description:** As I'm looking through the catalogue I noticed an item that I liked, I clicked on the item and it took me to a separate page that provided more detail for me to make an informed decision, I then added to cart and return to shopping. Later I told my friend about the website, and he accessed it from his phone to take a look at the item I ordered. He was impressed on how easy to use on mobile it was. 

## Glossary

In this section, you should list any terms that are used in the document that may not be immediately obvious to a naive reader. Each group member must supply at least one term. Each term should be written in the following format:

* **Term:** Compatability
  * **Definition:** A state in which two things are able to exist or occur together without problems or conflict.
