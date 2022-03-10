# DevOps-Core-Fundamental-Project

## Project Brief
 To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules covered during training.

## Idea
i want to create an application that can create football teams and add players to them. I also want to be able to delete players and teams and be able to update players and teams. I would also like to be able to view the players and teams. Below is the ERD for my project.

![ERD1](Images/football%20ERD.png)


In the future I would like to add more fields to my tables and also add a table for football managers and be able to add them to the teams. See ERD below. 

![ERD2](Images/future%20erd.png)

## CI Pipeline
The project required the use of parts of a CI pipeline. These included project tracking, version control, development environment and a build server. For project tracking I used Jira to create the project and a sprint. I created epics and added issues to them to keep track of the tasks I needed to complete. I also assigned story points and MoSCoW prioritisation to the issues. Below is an image of my Jira board at the start of the project. 
Here is a link to my jira project 
: (https://qawilliamderby.atlassian.net/jira/software/projects/DCFP/boards/3/backlog) 

![Jira board](Images/Jira%20Board.png)


For the version control I used git, with the project repository hosted on github. Git allows changes to the project to be made and committed while keeping a history of commits for access to an earlier version. Using GitHub as a repository hosting service allows the repo to be stored away from the development environment. GitHub can also provide webhooks that send http POST requests to the build server to automate building and testing. 

The development environment used was a python3 virtual environment (venv) hosted on a virtual machine. Python is used because Flask is a python-based framework. 

For the build server Jenkins was used. This allowed the building and testing to be automated. The automation works by setting up a freestyle project that executes the test.sh script when it receives a webhook from GitHub. If there is a change to the GitHub repo a new build will be automatically started by Jenkins. Jenkins was also used to run the app with gunicorn. Gunicorn allows multiple processes to run the app. 

![CI pipeline](Images/CI%20Pipeline.png)


## Risk Assessment
Before I started building the app I created a risk assessment to identify risks and propose measures to control them. The measures could be used if needed. See risk assessment bellow:
![Risk Assessment](Images/Risk%20assessment.png)

## Testing
Testing the app was a key part of the development process, first of all unit testing was needed to test the functionality of the app. I wrote tests for all of the CRUD functions to make sure they all worked. The goal of the unit tests was to get as high coverage as possible. 

I achieved 96% coverage from the unit tests.
![coverage report](Images/jenkins%20cov%20report.png)
The tests were automated using Jenkins via webhooks.
![automated tests](Images/Automated%20Tests%20with%20Jenkins.png)
There is also another type of testing, integration testing. Integration testing is a type of software testing in which we test the application as a whole, rather than mocking the application to it's routes as we do in unit testing. Selenium is used to simulate a user interacting with the application directly and test the results. Ideally this would have been implemented to ensure the app is fully functional and has no bugs. 

## The App
When the user navigates to the app the home page will be presented. On this page the user will be able to see already created teams with the players that are assigned to the team underneath. Aswell as this the user will have an option to delete a player as well as an option to update the player where they can change any attribute associated with the player. 
![homepage](Images/Screenshot%202022-03-09%20at%2009.33.37.png)

The user can navigate to the ‘Add a player’ page where a form to create a player will be presented. Here they can create a player and assign them to a team. 
![addplayerpage](Images/Screenshot%202022-03-09%20at%2009.34.35.png)

The final page a user can navigate to is the ‘Create a team’ page. Here a user can create a team that can later have players assigned to. 
![createateampage](Images/Screenshot%202022-03-09%20at%2009.34.42.png)

## Known Issues
- There is nothing stopping the same team being created again.
- There is nothing stopping the same player being created again.

## future Work
In the future there are a few features i would like to add. 
- A way to update and delete teams
- A new page to be able to create managers
- A way of seeing more of the player attributes
- Use integration testing

## Evaluation
Overall I am very happy about how my first Flask application has turned out. I have learned a lot throughout the process and can take what I have learned into future projects and work. I stuck to the brief and ended up with an application I am proud of. With more time and experience I believe I could add many more features to the app and implement integration testing with selenium.   