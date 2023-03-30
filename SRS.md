# Software Requirements Specification Document
Version 2
This serves as a template for each projects' Software Requirements Specification (SRS) document. When filling this out, you will be required to create user stories, use cases, requirements, and a glossary of terms relevant to your project. Each group member must contribute to every section, so it is crucial that your group's GitHub repository shows a commit history that reflects the work of each group member. It is highly recommended that you create separate branches for each member, but since this is one single document, you will need to manually merge the branches together. It is also advisable to have multiple working versions of this document (named separately) so that one person can compile the final SRS document from the multiple working versions. Ultimately, how you go about managing this is up to you, but consistent formatting, clear commit messages, and a thorough commit history with contributions from each group member are required.

Fill the document out following the guidelines listed in each section. Maintain [proper Markdown syntax](https://www.markdownguide.org/basic-syntax/) and be sure that your group has a `main` branch with this document and the entire [template repository codebase](https://github.com/david-gary/onlineStoreTemplate) either forked or downloaded and copied into your group's repository. If you have arranged to use a different codebase as a template, you do not need to have the original template included, but a `main` branch is still required.

## Group Members

* [Sreyas Kodukulla](mailto:skodukul.edu)
* [Akanimoh Joseph Umoren](mailto:aumoren@uncc.edu)
* [Blaise Thomas](mailto:bthom108@uncc.edu)
* [Mercere Baker](mailto:mbaker89@uncc.edu)

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

* **Constraint 1:** We cannot include recommended items because we can't collect the user data to narrow it down.
* **Constraint 2:** Stakeholders cannot choose from a very vast collection of items, our site will be limited to only the scope of items we can include. 
* **Constraint 3:** We do not display stakeholder reviews but we have admin reviews.
* **Constraint 4:** We do not control delivery prices because we deliver products using a third party delivery system.
* **Constraint 5:** No automated payments accepted, Only Debit/Credit Cards. Only Available to US Region
* **Constraint 6:** This project's code is written using Python, HTML, CSS, and Javascript.
* **Constraint 7:** The project has to be finished by the end of UNCC's 2023 spring semester.
* **Constraint 8:** 

## Use Cases

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

* **ID:** UC-5
  * **Description:** Making a singular webpage for each item with more depth of review and descriptions that also allows them to add to cart
  * **Actors:** I will be building the web page, and adding the extra descriptions, Mercer will be going behind me to make sure the webpage will link to the checkout page
  * **Preconditions:** Has to come from a previous page that was the items brief description, I.E Under the rings page it is the ring 3 Item, clicking that leads to the ring 3 Item webpage
  * **Postconditions:** You've landed on the webpage for that specific item, complete with the photo, description, and add to cart button. 

* **ID:** UC-6
  * **Description:** Making sure that the webpages works across all devices
  * **Actors:** I will be making sure that the customers can access the page from different devices, such as tablets, smartphones, and computers
  * **Preconditions:** Has a device that can display webpage
  * **Postconditions:** The webpage displays properly with no errors or loss in usability

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

* **ID:** US-1
  * **Type of User:** Customer
  * **Description:** The customer opens up the website, navigates to the filter search button because they are looking for a certain type of ring, they apply the filters, and they will be directed to the options we offer based on their preference.

* **ID:** US-2
  * **Type of User:** Customer
  * **Description:** The user navigates to the item they desire. Once they do that, they click on the image of the item and are shown a brief description about what the item is to aid them with their shopping experience.

* **ID:** US-3
  * **Type of User:** Customer
  * **Description:** The customer does not want to delete an item in cart that they do not want to purchase anymore. They click on the cart icon which lists the items in their cart and there is an option to remove each item from the cart. They successfully remove the item they do not need anymore.

* **ID:** US-4
  * **Type of User:** Customer
  * **Description:** The customer is currently viewing necklaces and wants to look at rings instead. They use the navigation bar to successfully got to the ring section.

* **ID:** US-5 Web page that displays the item, a description, and an add to cart button for the user to purchase. 
  * **Type of User:** Customer
  * **Description:** As I'm looking through the catalouge I noticed an item that I liked, I clicked on the item and it took me to a separate page that provided more detail for me to make an informed decision, I then added to cart and return to shopping.

* **ID:** US-6 Web page that displays properly regardless of the device used to acess it.
  * **Type of User:** Customer
  * **Description:** As I'm looking through the catalogue I noticed an item that I liked, I clicked on the item and it took me to a separate page that provided more detail for me to make an informed decision, I then added to cart and return to shopping. Later I told my friend about the website, and he accessed it from his phone to take a look at the item I ordered. He was impressed on how easy to use on mobile it was. 

* **ID:** US-7
  * **Type of User:** Customer
  * **Description:** The customer found our website and is interested in purchasing a piece of our jewelry. They browse the site, put an item in their shopping cart, click on the shopping cart icon, get taken to a checkout page, and confirm the order with an address and card information.

* **ID:** US-8
  * **Type of User:** IT
  * **Description:** The customer has a question about the website or has problems purchasing their items. They can send their issues to the provided email to have it checked out.


## Glossary

* **Term:** Filter Search
  * **Definition:** the filter search is when a user can input certain things that they are looking for and not looking for (based on price, material, type) and will find items that match the conditions they have set in the search.

* **Term:** Compatability
  * **Definition:** A state in which two things are able to exist or occur together without problems or conflict.

* **Term:** shopping cart
  * **Definition:** software to allow customers to select products and buy them on the web.

* **Term:** Navigation bar
  * **Definition:** The webpage element that helps users navigate through the use of hyperlinks.