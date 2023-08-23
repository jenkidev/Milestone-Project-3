# Bridgend Eagles Team Website
(by Morgan Jenkins)

## Table of Contents

1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requirements and Expectations](#user-requrements-and-expectations)
    3. [User Stories](#user-stories)
    4. [Scope](#scope)
3. [Design of Site](#design-of-site)
    1. [Initial Idea](#initial-idea)
    2. [Wireframes](#wireframes)
    3. [Site Layout](#site-layout)
    4. [Colour Choices](#colour-choices)
    5. [Fonts](#fonts)
    6. [Database Structure](#database-structure)
    7. [MongoDB Collection](#mongodb-collections)
4. [Technologies Implemented](#technologies-implemented)
    1. [Languages](#languages)
    2. [Tools](#tools)
5. [Site Features](#site-features)
6. [Testing](#testing)
    1. [Validation](#validation)
        1. [HTML Validation](#html-validation)
        2. [CSS Validation](#css-validation)
        3. [JavaScript Validation](#javascript-validation)
    2. [Performance and Accessibility](#performance-and-accessibility)
    3. [Device Tests](#device-tests)
    4. [Responsiveness](#responsiveness)
    5. [User Story Tests](#user-story-tests)
7. [Bug Squashing](#bug-squashing)
8. [Deployment](#deployment)
    * [Deploying to Github Pages](#deploying-to-github-pages)
    * [Forking the githubrepository](#forking-the-github-repository)
    * [Cloning the repository](#cloning-the-github-repository)
9. [Credits](#credits)
10. [Thank You](#thank-you)


## Project Goals

### User Goals

* To read the latest news on the Bridgend Eagles basketball team.
* To view upcoming and past fixtures for the Bridgend Eagles basketball team.
* To sign up to the site as a registered user.
* To send an email to the site owner through a dedicated contact form.
* Once signed in, to be able to view the players of the team along with their stats.

### Site Owner Goals

* To have access to the admin account.
* To view, add, update and delete articles.
* To view, add, update and delete players.
* To view, add, update and delete fixtures.


## User Experience

### Target Audience

* Fans of the Bridgend Eagles Basketball. team.
* Players of the Bridgend Eagles Basketbal teaml
* People who wish to join the Bridgend Eagles Basketball team.
* Senior memebership/administrators of the team.

### User Requirements and Expectations

* Easy to navigate site and intuitive design.
* Clear and simple information about the team.
* The ability to interact with all information stored in the database relevant to the team following the CRUD methodology.
* Responsive design that adapts to mobile, tablet and desktop.
* Easy to fill out contact form.

### User Stories
#### First-time User 

1. I want to view news relevant to the Bridgend Eagles basketball team.
2. I want to view the fixtures for the Bridgend Eagles basketball team.
3. I want to see the training times for team.
4. I want to contact the team via email.
5. I want to register as a user to the site.
6. I want to view social media relevant to the team.

#### Returning User

7. I want to view the fixtures for the Bridgend Eagles basketball team.
8. I want to see the training times for team.
9. I want to sign into the site using a created account.
10. I want to view the players on the team and their statistics.

#### Site Owner 

11. I want to add new articles.
12. I want to edit existing articles.
13. I want to delete an article.
14. I want to add new fixtures.
15. I want to edit existing fixtures.
16. I want to delete an fixture.
17. I want to add new players.
18. I want to edit existing players.
19. I want to delete an player.
20. I want to sign into an account with admin permissions.
21. I want to receive emails from users that fill out the relevant form.

## Scope

The scope of the project in it’s first release is defined by the following features:

* Landing page with a clear navigation menu that can take unregistered users to News, Fixtures and a Contact form.
* Site must connect to MongoDB and display documents from the collection in a clear front end manner.
* Registered users can see player information. This protects personal information from unregistered users.
* Admin account is able to interact with all database information displayed using CRUD functionality.
* Allow User to sign in to the site or register if they are not already.
* Fully functional contact form with emailJS that will not submit unless all fields are filled out.
* A 404 error page that is styled and allows navigation back to the main page.
* A 500 error page in the event of a server error that is fully styled and directs back to the main page.
* Clear favicon that shows the site logo.

## Design of Site

### Initial idea

The main purpose of this site was to create a front end that would display collections from MongoDB. I decided to create a fake basketball team called the Bridgend Eagles (my local town). The Database would display news articles, players and fixtures of the team. An admin account would have permissions to update, delete and create new records. It would be fully responsive for desktop, tablet and mobile and would have a connection to the emailJS API to allow users to contact the site owner.

### Wireframes

To create the wireframes for this site I used the balsamiq cloud service. This allowed me to create a more basic wireframe. This was helpful as I have found in the past having a more complex and detailed wireframe to be quite restricting. 

<details><summary>Home Page Wireframe (news) - Mobile</summary><img src="docs/wireframes/Fixtures Page Mobile.png"></details><br>

<details><summary>Home Page Wireframe (news) - Tablet</summary><img src="docs/wireframes/Home Page Tablet.png"></details><br>

<details><summary>Home Page Wireframe (news) - Desktop</summary><img src="docs/wireframes/Home Page Desktop.png"></details><br>

<details><summary>Players Page - Mobile</summary><img src="docs/wireframes/Players Page Mobile.png"></details><br>

<details><summary>Players Page Wireframe - Tablet</summary><img src="docs/wireframes/Players Page Tablet.png"></details><br>

<details><summary>Players Page Wireframe - Desktop</summary><img src="docs/wireframes/Players Page Desktop.png"></details><br>

<details><summary>Fixtures Page Wireframe - Mobile</summary><img src="docs/wireframes/Fixtures Page Mobile .png"></details><br>

<details><summary>Fixtures Page Wireframe - Tablet</summary><img src="docs/wireframes/Fixtures Page Tablet.png"></details><br>

<details><summary>Fixtures Page Wireframe - Desktop</summary><img src="docs/wireframes/Fixtures Page Desktop.png"></details><br>

<details><summary>Contact Page Wireframe - Mobile</summary><img src="docs/wireframes/Contact Page Mobile.png"></details><br>

<details><summary>Contact Page Wireframe - Tablet</summary><img src="docs/wireframes/Contact Page Tablet.png"></details><br>

<details><summary>Contact Page Wireframe - Desktop</summary><img src="docs/wireframes/Contact Page Desktop.png"></details><br>

### Site Layout

The Site will have four main pages and these will be the news page, fixtures page, players page and contact page. These pages will be accessed via a nav bar at the top of the page. There will be two other sub pages a registration page and a sign in page and one more link in the nav bar where users can sign out.

#### News Page- 

#### Fixtures Page- 

#### Players Page-

#### Contact Page

#### SignIn and Registration Pages-

#### Sign Out Link- 


### Colour Choices


### Fonts
The font used for the site is the "Exo" font as this had quite a bold and easy to read style whilst also being curved, thus giving the website an approachable feel.

## Technologies Implemented

### Languages

### Tools

## Site Features

## Testing
    
### Validation

#### HTML Validation- W3C markup validation service was used to assess the validity of my HTML code.




#### CSS Validation- W3C CSS validation service was used to assess the validity of my CSS code



#### JavaScript Validation- JS hint was used to assess the validity of my scripts



### Performance and Accessibility

Google Lighthouse as part of the Chrom dev tools was used to assess performance and accessibility.


### Device Tests

The website was tested on the following devices:
* Samsung Galaxy M31
* iPhone 12 Pro
* Ipad Pro 4th Gen
* Asus Vivobook laptop (X515JAB_X515JA)

### Responsiveness

[Responsinator](http://www.responsinator.com/?url=jenkidev.github.io%2FMilestone_project_2%2F) was used to assess the responsiveness of the project. 

### User Story Tests

1. I want to view news relevant to the Bridgend Eagles basketball team.


| **Feature Used** | **User Action** | **Expectation** | **Result** |
| ---------------- | --------------- | --------------- | ---------- |
|  |  |  |  |

2. I want to view the fixtures for the Bridgend Eagles basketball team.

| **Feature Used** | **User Action** | **Expectation** | **Result** |
| ---------------- | --------------- | --------------- | ---------- |
|  |  |  |  |

3. I want to see the training times for team.

| **Feature Used** | **User Action** | **Expectation** | **Result** |
| ---------------- | --------------- | --------------- | ---------- |
|  |  |  |  |

4. I want to contact the team via email.

| **Feature Used** | **User Action** | **Expectation** | **Result** |
| ---------------- | --------------- | --------------- | ---------- |
|  |  |  |  |

5. I want to register as a user to the site.

| **Feature Used** | **User Action** | **Expectation** | **Result** |
| ---------------- | --------------- | --------------- | ---------- |
|  |  |  |  |

6. I want to view social media relevant to the team.

| **Feature Used** | **User Action** | **Expectation** | **Result** |
| ---------------- | --------------- | --------------- | ---------- |
|  |  |  |  |


#### Returning User

7. I want to view the fixtures for the Bridgend Eagles basketball team.

| **Feature Used** | **User Action** | **Expectation** | **Result** |
| ---------------- | --------------- | --------------- | ---------- |
|  |  |  |  |

8. I want to see the training times for team.

| **Feature Used** | **User Action** | **Expectation** | **Result** |
| ---------------- | --------------- | --------------- | ---------- |
|  |  |  |  |

9. I want to sign into the site using a created account.

| **Feature Used** | **User Action** | **Expectation** | **Result** |
| ---------------- | --------------- | --------------- | ---------- |
|  |  |  |  |

10. I want to view the players on the team and their statistics.

| **Feature Used** | **User Action** | **Expectation** | **Result** |
| ---------------- | --------------- | --------------- | ---------- |
|  |  |  |  |

#### Site Owner 

11. I want to add new articles.

| **Feature Used** | **User Action** | **Expectation** | **Result** |
| ---------------- | --------------- | --------------- | ---------- |
|  |  |  |  |

12. I want to edit existing articles.

| **Feature Used** | **User Action** | **Expectation** | **Result** |
| ---------------- | --------------- | --------------- | ---------- |
|  |  |  |  |

13. I want to delete an article.

| **Feature Used** | **User Action** | **Expectation** | **Result** |
| ---------------- | --------------- | --------------- | ---------- |
|  |  |  |  |

14. I want to add new fixtures.

| **Feature Used** | **User Action** | **Expectation** | **Result** |
| ---------------- | --------------- | --------------- | ---------- |
|  |  |  |  |

15. I want to edit existing fixtures.

| **Feature Used** | **User Action** | **Expectation** | **Result** |
| ---------------- | --------------- | --------------- | ---------- |
|  |  |  |  |

16. I want to delete an fixture.

| **Feature Used** | **User Action** | **Expectation** | **Result** |
| ---------------- | --------------- | --------------- | ---------- |
|  |  |  |  |

17. I want to add new players.

| **Feature Used** | **User Action** | **Expectation** | **Result** |
| ---------------- | --------------- | --------------- | ---------- |
|  |  |  |  |

18. I want to edit existing players.

| **Feature Used** | **User Action** | **Expectation** | **Result** |
| ---------------- | --------------- | --------------- | ---------- |
|  |  |  |  |

19. I want to delete an player.

| **Feature Used** | **User Action** | **Expectation** | **Result** |
| ---------------- | --------------- | --------------- | ---------- |
|  |  |  |  |

20. I want to sign into an account with admin permissions.

| **Feature Used** | **User Action** | **Expectation** | **Result** |
| ---------------- | --------------- | --------------- | ---------- |
|  |  |  |  |

21. I want to receive emails from users that fill out the relevant form.

| **Feature Used** | **User Action** | **Expectation** | **Result** |
| ---------------- | --------------- | --------------- | ---------- |
|  |  |  |  |


## Bug Squashing

| **Bug** | **Fix** |
|---------|---------|
When using the delete functionality for fixtures.html after selecting to delete on the confirmation modal a different collapsible selection would open and then get deleted as that was the active ID. | I am not sure why this happens as there is no trigger being clicked on I can only assume it is an interaction between the modal and collapsible classes of Materialize. Therefore in this case I have moved the delete fixture button to the edit_fixture.html page as this is only accessible to the admin and bypasses the bug.

## Deployment

### Deploying to GitHub Pages



### Forking the GitHub Repository



### Cloning the GitHub Repository



## Credits



## Thank You

* My mentor Antonio Rodriguez for his help and advice in creating this project.
* To the team at [Code Institute](https://codeinstitute.net/) for the lessons and support.
* My Partner for helping with project testing and supporting me through it.