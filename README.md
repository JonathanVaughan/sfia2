# Holiday Generator

## Contents
* Brief
* Project Proposal
* Trello Board

## Project Brief
Create an application that generates “Objects” upon a set of predefined rules.
Some of the requirements 
* 

## Project Proposal
I decided to create a holiday generator for my application which would generate A random Country and a random activity to be displayed through a front end website.

The application was made up of 4 microservices working together:
##### Service 1
This service is the frontend of the website. Its a lightweight flask application with 1 HTML template which displays the generated holiday and activity. 
It also shows persistence of data by displaying all previously generated combonations below pulling them down from an SQL table.
##### Service 2
Generates a random Country from a predefined SQL table.
##### Service 3
Generates a random Activty from a predefined SQL table.
##### Service 4
Makes a request to service 2 and 3 and adds them both to final SQL table
Puts the collected requests from service 2 and 3 into a string ready to be sent to service 1

## Trello Board
For my project I utilised a kanban Trello board. This helped me tack each stage of my project adding on new tasks and tracking my development stage as I created my application helpinh me improve overall efficiency.

### Before Completion
Shown below is my intial trello board:
![](images/Trellostart.PNG)

### Mid development

### After Completion

## Risk Assesment
Before starting work on my application an initial risk assesment was created shown below
![](images/RiskA.PNG)

### Revisited
After Completing the project I revisited the risk assesment and commented on wether or not i had encountered the inital risk.
Revisited Risk assesment shown below:
![](images/RiskB.PNG)

## Entity Relationship Diagram
![](images/ERD.PNG)

