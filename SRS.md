# Software Requirements Specification Document

This serves as a template for each projects' Software Requirements Specification (SRS) document. When filling this out, you will be required to create user stories, use cases, requirements, and a glossary of terms relevant to your project. Each group member must contribute to every section, so it is crucial that your group's GitHub repository shows a commit history that reflects the work of each group member. It is highly recommended that you create separate branches for each member, but since this is one single document, you will need to manually merge the branches together. It is also advisable to have multiple working versions of this document (named separately) so that one person can compile the final SRS document from the multiple working versions. Ultimately, how you go about managing this is up to you, but consistent formatting, clear commit messages, and a thorough commit history with contributions from each group member are required.

Fill the document out following the guidelines listed in each section. Maintain [proper Markdown syntax](https://www.markdownguide.org/basic-syntax/) and be sure that your group has a `main` branch with this document and the entire [template repository codebase](https://github.com/david-gary/onlineStoreTemplate) either forked or downloaded and copied into your group's repository. If you have arranged to use a different codebase as a template, you do not need to have the original template included, but a `main` branch is still required.

## Group Members

* [Vishal Dasari](mailto:vdasari1@uncc.edu)

## Revisions

When a change is made to the document, a new revision should be created. The revision should be added to the table below with all information filled out.

| Version | Date | Description | Author | Reviewed By |
| --- | --- | --- | --- | --- |
| 1.0 | 03/22/23 | Initial draft | [David Gary](mailto:dgary9@uncc.edu) | [David Gary](mailto:dgary@uncc.edu) |
| 1.1 | 04/23/23 | Added Name    | [Vishal Dasari](mailto:vdasari1@uncc.edu) | [Vishal Dasari](mailto:vdasari1@uncc.edu) |
| 1.2 | 05/2/23 | Worked on Table of Contents (1-3)    | [Vishal Dasari](mailto:vdasari1@uncc.edu) | [Vishal Dasari](mailto:vdasari1@uncc.edu) |
| 1.3 | 05/5/23 | Worked on Table of Contents (4-6)    | [Vishal Dasari](mailto:vdasari1@uncc.edu) | [Vishal Dasari](mailto:vdasari1@uncc.edu) |

## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Constraints](#constraints)
4. [Use Cases](#use-cases)
5. [User Stories](#user-stories)
6. [Glossary](#glossary)

## Introduction
In this section, you should give a brief overview of what your project will be. Describe the software system you are building and what problems it solves. You should also give a short description of the stakeholders (users of the system) and what their needs are. There is no set formatting requirement, but you should maintain a consistent structure across future sections. Not all members must contribute to this section.

The software system that I will be building is an online gaming store.  The program would display an image of the games a user could buy or rent.  Stakeholders would be the users who would like to buy/rent the video games out.  The stakeholder's needs would be the item that they would like to acquire.

## Requirements

Each group member must supply at least three functional requirements for the project. Each requirement should be written in the following format:

**REQ-1:** Allow users to create an account and login.
  * **Description:** To access an existing user information.
  * **Type:** Functional
  * **Priority:** 1 
  * **Rationale:** Users need an account to purchase/rent games and access their saved games.
  * **Testing:** Ensure the username and the password matches with our server
* **REQ-2:** Creating New Account
  * **Description:** To have access to the respected user's page.
  * **Type:** Functional
  * **Priority:** 1
  * **Rationale:** Needed to access user's account
  * **Testing:** Create an account and verify that login works as expected.
* **REQ-3: Display a list of available games for purchase/rental**
  * **Description: User will be able to look at the latest updates games available**
  * **Type:** Functional
  * **Priority:** 1
  * **Rationale:** This is the core functionality of the system.
  * **Testing:** Ensure that the list of games displayed is accurate and up-to-date.
* **REQ-4: Allow users to add game(s) to the shopping cart**
  * **Description: To have access to adding games to your shopping cart.
  * **Type:** Functional. 
  * **Priority:** 1
  * **Rationale:** Users may want to save games for later or purchase multiple games at once.
  * **Testing:**  Add a game to the cart/wish list and verify that it is displayed in the appropriate section.
* **REQ-5**: Allow users to filter games based on genre.
  * **Description:** User will be able to filter thorugh different genres.
  * **Type:** Functional
  * **Priority:** 2
  * **Rationale:** Users may want to browse games within a specific genre.
  * **Testing:** Check if the filter displays only games that match the selected genre.
* **REQ-6**: Allow users to search for games by title or keyword.
  * **Description**: Displays current book info
  * **Type:** Functional
  * **Priority:** 2
  * **Rationale:** Users may want to search for specific games they have in mind.
  * **Testing:** Search for a known game title and verify that it is displayed in the search results.
* **REQ-7** Display game details such as title, description, release date, and rating.
  * **Description:** Allows users to learn more about the game, ratings, and price etc.
  * **Type:** Functional
  * **Priority:** 2
  * **Rationale:** Users need to know more about a game before deciding to purchase/rent it.
  * **Testing:** Verify that game details displayed are accurate and match the selected game.
* **REQ-8** Allow users to view their order history.
  * **Description:** Displays user's order history.
  * **Type:** Fuctional
  * **Priority:** 2
  * **Rationale:** Users may want to view past purchases or rentals.
  * **Testing:** Verify that the order history displays accurate information about past purchases/rentals.
* **REQ-9** Rate/Review games.
  * **Description:** Allow users to rate and review games.
  * **Type:** Functional
  * **Priority:** 3
  * **Rationale:** User reviews and ratings can help other users make informed decisions.
  * **Testing:** Verify that users can rate and review games, and that the ratings and reviews are displayed correctly.
* **REQ-10** Provide customer support and contact information
  * **Description:** Provides customer support and contact information to the user
  * **Type:** Functional
  * **Priority:** 4
  * **Rationale:** Users may need help with purchasing or rental issues.
  * **Testing:** 	Verify that the customer support and contact information is accurate and up-to-date.
* **REQ-11** Shipping Information
  * **Description:** Asks user to enter your shipping information.
  * **Type:** Functional
  * **Priority:** 4
  * **Rationale:** Users will get this option at the time of the payment.
  * **Testing:** Enter the shiping information and see that it shows in the system.
* **REQ-12** Payment Method/Information
  * **Description:** Asks the user for their payment information.
  * **Type:** `Functional`
  * **Priority:** 4
  * **Rationale:** It is one of the last steps for buying a game.
  * **Testing:** Verify the payment information in the system.

## Constraints

In this section, you should list any constraints that you have for the project. Each group member must supply at least two constraints. These can be constraints on the project itself, the software system, or the stakeholders. Constraints can be anything that limits the scope of the project. For example, that this project's template code is written using Flask and Python constitutes a constraint on the backend of the project. Constraints can also be things like the required timeline of the project. Be creative.

* **Constraint 1:**
I am able to use either python, html, javascript, or flask only.
* **Constraint 2:**
I am working alone in this project
* **Constraint 3:**
No discussion or guidance from my groupmates for any cross-reference.
* **Constraint 4:**
The website should not crash
* **Constraint 5:**
The entire project should be finished within last day of final project submission.

## Use Cases

In this section, you should list use cases for the project. Use cases are a thorough description of how the system will be used. Each group member must supply at least two use cases. Each use case should be written in the following format:

* **UC-1:** User Account Creation
  * **Description:** A new user creates an account to access the system.
  * **Actors:** User
  * **Preconditions:**  None
  * **Postconditions:** The user has successfully created an account and can log in to the system.
* **UC-2:** User Login
  * **Description:** An existing user logs into their account to access the system.
  * **Actors:** User
  * **Preconditions:** The user must have already created an account.
  * **Postconditions:** The user has successfully logged in and can access their account page.
* **UC-3:** Browse Games
  * **Description:** A user browses through the available games on the system.
  * **Actors:** User
  * **Preconditions:** The user must be logged in.
  * **Postconditions:** The user has browsed through the available games and can view more details about a specific game.
* **UC-4:** Purchase/Rent Game
  * **Description:** A user purchases or rents a game.
  * **Actors:** User
  * **Preconditions:** The user must be logged in and have selected a game to purchase or rent.
  * **Postconditions:** The user has successfully purchased or rented a game and can access it in their account.
* **UC-5:** View Order History
  * **Description:** A user views their order history.  
  * **Actors:** User
  * **Preconditions:** The user must be logged in and have made previous purchases/rentals.
  * **Postconditions:** The user has successfully viewed their order history.
* **UC-6:** Provide Customer Support
  * **Description:** A user contacts customer support for assistance.
  * **Actors:** User, Customer Support Representative
  * **Preconditions:** The user must be logged in and have an issue that requires assistance.
  * **Postconditions:** The user's issue is resolved or a solution is provided to the user.
* **UC-7:** Enter Shipping Information
  * **Description:** User enters shipping information during the checkout process.
  * **Actors:** User
  * **Preconditions:** User has selected the game they wish to purchase and has proceeded to the checkout process.
  * **Postconditions:** User's shipping information is saved in the system and is displayed on the order confirmation page.
 * **UC-8:** Enter Payment Information
  * **Description:** User enters payment information during the checkout process.
  * **Actors:** User
  * **Preconditions:** User has selected the game they wish to purchase, has entered their shipping information, and has proceeded to the payment section of the checkout process.
  * **Postconditions:** User's payment information is saved in the system, the payment is processed, and the user is redirected to the order confirmation page.

## User Stories

In this section, you should list user stories for the project. User stories are a short description of how a user will be interacting with the system. Each group member must supply at least two user stories. Each user story should be written in the following format:

* **US-1:**
  * **Type of User:** Customer
  * **Description:** As a customer, I want to be able to filter games by genre so that I can find games that fit my interests easily. I expect to see a list of games that match my chosen genre.
* **US-2:** 
  * **Type of User:** Customer
  * **Description:** As a customer, I want to be able to search for games by title so that I can find a specific game I'm interested in. I expect to be able to see the game's details once I've found it.
* **US-3:** 
  * **Type of User:** Customer
  * **Description:** As a customer, I want to be able to see the system requirements for a game so that I can determine if my computer can run it. I expect to see a clear list of minimum and recommended requirements.
* **US-4:** 
  * **Type of User:** Customer
  * **Description:** As a customer, I want to be able to read reviews and ratings from other users before deciding to purchase or rent a game. I expect to see an overall rating and a selection of reviews.
* **US-5:** 
  * **Type of User:** Customer
  * **Description:** As a customer, I want to be able to see my cart's contents at all times and the total cost so that I can keep track of my purchases. I expect to be able to easily remove items from my cart if needed.

## Glossary

In this section, you should list any terms that are used in the document that may not be immediately obvious to a naive reader. Each group member must supply at least one term. Each term should be written in the following format:

* **Term:** User
  * **Definition:** A person who interacts with the system to browse and purchase games.
* **Term:** Account
  * **Definition:** A user's personal profile in the system that contains their personal information and order history.
* **Term:** Checkout Process
  * **Definition:** The series of steps that a user must follow to complete a purchase or rental of a game, including entering shipping and payment information.
* **Term:** Customer Support Representative
  * **Definition:** An individual who assists users in resolving issues and answering questions related to the system
