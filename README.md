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


#### Site Owner 


## Scope


## Design of Site

### Initial idea


### Wireframes

To create the wireframes for this site I used the balsamiq cloud service. This allowed me to create a more basic wireframe. This was helpful as I have found in the past having a more complex and detailed wireframe to be quite restricting. 

<details><summary>Home Page Wireframe (news) - Mobile</summary><img src="docs/wireframes/Home Page Mobile.png"></details><br>

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



### Colour Choices


### Fonts


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

#### First-time User 


| **Feature Used** | **User Action** | **Expectation** | **Result** |
| ---------------- | --------------- | --------------- | ---------- |


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