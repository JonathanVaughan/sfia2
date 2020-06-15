# Holiday Generator

## Contents
* Brief
* Project Proposal
* Trello Board
* Risk assesment
* Entity Relationship Diagram
* Service Architecture Diagram
* System Security
* Pipeline 
* Testing
* Design
* Improvements for future
* Installation Guide
* Authors
* Acknowledgements

## Project Brief
Create an application that generates “Objects” upon a set of predefined rules.
Some of the requirements 
* A Kanban board
* Version control system
* Deployed to a cloud based VM
* Use a webhook
* Follow service oriented architecture
* Deployed using an orchestration and containerisation tool
* Ansible Playbook should provision the environment

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
Key for Trello Board  
Green: Must Have  
Yellow: Should Have  
Orange Could Have
Red: Would Have  
## Trello Board
For my project I utilised a kanban Trello board. This helped me tack each stage of my project adding on new tasks and tracking my development stage as I created my application helpinh me improve overall efficiency.

Link to trello board: https://trello.com/b/l9sU6poy/sfia2

### Before Completion
Shown below is my intial trello board:
![](images/Trellostart.PNG)

### After Completion
![](images/Trelloend.PNG)

## Risk Assesment
Before starting work on my application an initial risk assesment was created shown below
![](images/RiskA.PNG)

### Revisited
After Completing the project I revisited the risk assesment and commented on wether or not i had encountered the inital risk.
Revisited Risk assesment shown below:
![](images/RiskB.PNG)

## Entity Relationship Diagram
![](images/ERD.png)
For my project I used 3 tables as you can see above

The Country table has 10 random countrys for service 2 to randomly pull down

The Activity table has 10 random activitys for service 3 to randomly choose from

The plan table gets the randomly pulled objects from in service 4 and adds them to a table in the home page, this also shows persistence of data.


## Service Architecture Diagram
![](images/Flow.png)
#### Service 1
Responsible for everything the user sees. Through the use of HTML, Jinja2 and Flask, This service Displays the generated data from service 2 and 3. It also displays information from the SQL table made in service 4 displaying previously generated combonations

#### Service 2 and 3
Generate a random object to be returned

#### Service 4
Service 4 requests the generated objects from service 2 and 3, combines them into a string and returns the string ready to be requested from service 1
It also adds the output from service 2 and 3 to an SQL table to be displayed on service 1

## System Security
![](images/nginx.PNG)
A large part of this project is focused on security. Various methods taught in lectures have been used to disguise sensitive information from the world. NGINX allowed me to listen for ports in use and redirect / hide them from anyone outside of the network.
The NGINX config that i setup for my listens for requests on port 80 and internally redirects it to my service 1 on port 5000.

## Pipeline 
![](images/pipeline.png)  
The code for my project was written in vscode using its SSH extenstion it is then pushed to GitHub. Jenkins detects a new push to master with the use of a webhook. Using custom shell scripts and a Jenkins file, Jenkins builds each of the services and deploys the application. The application is deployed by docker swarm and stack, this distributes the workload between the manager and the worker node. Jenkins is also setup so that whenever new code is pushed to the master it will automatically build and push the newest version of the images to DockerHub.

#### Used technologies and languages
* Github: Version Control System
* Trello Board: Project Tracking
* Jenkins: CI Server
* Ansible: Configuration Management
* Google Cloud Platform: Live Environment and SQL Database
* Visual Studio Code: IDE using the following languages:
    * Python3
    * HTML
    * CSS
    * Flask
    * Jinja2
    * MYSQL
* Docker: Containerisation
* Docker Swarm and Docker Stack: Orchestration
* DockerHub: Version Control for docker images
* NGINX: Security and Load-balancing
* SQL Alchemy

## Testing
For testing PYTEST was used 
I was able to conduct tests for each function of the application, however due to the project utilising micro-services I was unable to unable to test some functions of the application. An attempt to utilise mocking was made (Shown below) unfortunately due to time constriants I was unable to test these features.
![](images/mocking.PNG)  
I was unable to implement testing with selenium due to time constraints.
### Coverage Report for each service:
##### Service 1
![](service1/test-results/service1results.PNG)
##### Service 2z
![](service2/test-results/service2results.PNG)
##### Service 3
![](service3/test-results/service3results.PNG)
##### Service 4
![](service4/test-results/service4results.PNG)#

## Design
![](images/Home.PNG)  
This was my front end for my project on service 1.
It displays the generated string from service 4 at the top and previous generations below.

## Improvements for future
1. Work more on the overall design of the website
2. Allow the user to apply filters and some choice such as specify a region or a type of activity.
3. Gain better overall knowledge of the used tools to produce a more effective and efficient final product
4. Add CRUD functionality to my project
5. Effective use of GitHub branches as on my last project I lost marks as my master branch was ahead of my developer due to working on the readme from thhe master.

## Installation Guide
### Prerequisites
* 2 webservers running on Ubuntu 18.04
* MYSQL server
* SSH keys configured so both webservers can communicate
### Steps
1. Install Jenkins on manager node
2. Clone Github repo (https://github.com/JonathanVaughan/sfia2.git)
3. Configure inventory.cfg for your nodes
4. Enable jenkins
5. Add user and jenkins ssh keys from manager into worker

## Authors
Jonathan Vaughan

## Acknowledgements
My fantastic trainers at QA and my good friends in group 4.

