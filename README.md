# The Lab

The live site can be viewed here [The LAB](https://the-lab.herokuapp.com/)!

![Mutli Device Screenshot](https://github.com/johndbigboi/The-Fitness-Lab/blob/master/static/images/multidevices.png)


Welcome to The Lab,

My goal with this project was to build a website using DJANGO with funtionality of an online store, blog and membership options available. I wanted to provide functions which allows users to add, edit, and delete. I wanted to build a website for a gym which provides various exercise classes , showing timetables of classes and brief descriptions of the classes on offer. The store shows exercise equipment for sale and allows purchases. In addition users can complete membership on the website with monthly and annual options available.

When it comes to shopping on the web, users need to feel safe & comfortable in order for them to actually go through with purchases online. Therefore providing the best UX, proper authentication and using secure payment gateways (in this case Stripe) is necessary to offer the best solution.

Thank you for visiting my Github page. I hope you enjoy reading about the project below. Please feel free to contact me with any questions or suggestions. You can message me through my Github page.

## Contents:

* [The Lab](#the-lab)
* [UX (User Experience)](#ux-user-experience)
    * [Project Goals](#project-goals)
        * [Target Audience Goals](#target-audience-goals)
        * [Site Owner Goals](#site-owner-goals)
        * [User Goals](#user-goals)
        * [User Stories](#user-stories)
    * [User Requirements and Expectations](#user-requirements-and-expectations)
        * [Requirements](#requirements)
        * [Expectations](#expectations)
    * [Design Choices](#design-choices)
        * [Icons](#icons)
        * [Images](#images)
        * [Colours](#colours)
        * [Defensive Design](#defensive-design)
    * [Wireframes](#wireframes)
    * [Database Design](#database-design)
    * [Features](#features)
    * [Technologies Used](#technologies-used)
        * [Languages](#languages)
        * [Libraries & Tools](#libraries-tools)
        * [Databases](#databases)
    * [Planning and Testing](#planning-and-testing)
        * [Feature Testing](#feature-testing)
        * [Further testing](#further-testing)
        * [Validators and linters](validators-and-linters)
    * [Deployment](#deployment)
        * [The following steps were taken to deploy The LAB on Heroku](#deploying-the-lab-to-heroku)
        * [Cloning The LAB from GitHub to Run Locally](#cloning-the-lab-from-gitHub)
  * [Bugs](#bugs)
  * [Credits](#credits)
  * [Disclaimer](#disclaimer)

## UX (User Experience):👍🏽

### Project Goals:

The Lab is milestone project for Code Institute Full Stack Frameworks with Django module.

<strong>The Lab</strong> is developed by using HTML, CSS, Jquery, Javascript, Python Django.

### Target Audience Goals:

* For health enthusiasts who are looking for a place to train.
* For people wants to purchase home gym equipements and gym gears.
* For Athletes where they can use a world class facilities.
* A website for health enthusiasts where they can contribute and connect with other users.

### Site Owner Goals:

* A website which is visually appealling and easy to navigate pages.
* Encourage user sales with promotions and discounts.
* Build awareness for the brand and attract companies on health and nutrition related products.
* Provides users with a safe and secure mode of payments.


### User Goals:

As a gym guest/Non-member user:

* As a user, I want to have access to information about different membership.
* As a user, I can purchase gym equipement and gym gears without login.
* As a user, I can easily contact the gym through the contact page for training inquiry.
* As a user, I can read the gym facilities reviews from other members.

As a gym member user:

* As a user, I can easliy navigate the website on any device (mobile/tablet/desktop).
* As a user, I can access the full functionality of the website.
* As a user, I can securely purchase and track orders through my account profile.
* As a user, I have access to workout videos exclusive only to members.
 

### User Stories:

#### Mr. Columbu: 
* <em>"As a user, I want a gym with a full functionality where you can buy gym gears and train without any hassle to look for a separate shops."</em>

#### Mr. Coleman: 
* <em>"As user and a very busy person, I want a website that I can navigate easily to book for gym classes while im on the move."</em>

#### Ms. Cutler: 
* <em>"As a user and a personal trainer, I wanted to share my knowledge on training videos I can post on the website."</em>

## User Requirements and Expectations: 🎯

#### Requirements:

*  Navigate the website with ease, and with fast loading time.
*  Can see profiles/user dashboard with all the information.
*  Add products to a shopping cart & update the cart quantities.
*  User can browse, submit, edit and Blog post.
*  Purchase products in the shopping cart in a safe and secure way.
*  Interact with a visually appealing website.


##### Expectations:

* The users payment information will be safe and will not be stored in the website's database.
* User Interface easy to navigate with search functions.
* The website loads with sufficient speed.
* The content on the website renders correctly on desktop, mobile and tablet.
* Content is visually satisfying and informative.
* The user feels informed and satisfied with the information available.



## Design Choices: 🎨

The design of this website was inspired from [PLATE FIT](https://platefit.co/) and based on Code Institute [boutique ado](https://github.com/ckz8780/boutique_ado_v1) E-commerce website for products and shop development.


#### Icons:

All icons used in the site were taken from [Font Awesome](https://fontawesome.com/) and [flaticon](https://www.flaticon.com/).

#### Images:

All background and images were taken from [freepick](https://www.freepik.com/) and [shutterstock](https://www.shutterstock.com/image-photo/modern-gym-interior-equipmentfilter-image-414548209). I used the [Pixlr](https://pixlr.com/) to edit the images for their own purposes.

#### Colours:

I used [this](https://www.color-hex.com/color-palette/42360) colour palette from color-hex.com.

![color palette](https://github.com/johndbigboi/The-Fitness-Lab/blob/master/static/images/colorpallette.png)

#### #ffd90f(School Bus Yellow):

![#ffd90f](https://via.placeholder.com/15/ffd90f/000000?text=+) `#ffd90f`
* Background colour of all box.
* Background colour of buttons.
* Font colour of the Title.


#### #fffff(White):

![#fffff](https://via.placeholder.com/15/ffffff/000000?text=+) `#ffffff`
* Font colour of the Title.
* colour of the border.


#### #000000(Rich Black):

![#000000](https://via.placeholder.com/15/000000/000000?text=+) `#000000`
* Font colour of the forms.
* Font colour of the all fonts.
* Background colour footer.
* Background colour Overlay.


#### #FF7F00(Dark Orange):

![#ff7f00](https://via.placeholder.com/15/ff7f00/000000?text=+) `#ff7f00`
* Background colour of buttons.
* Background colour of hover effects buttons.

#### Defensive design:

* All forms handle empty input fields by warning the user and not permitting recipe submission.
* User is given a message/alert feedback for actions/errors.
* User is not able to break the site by clicking buttons out of the expected order.

## Wireframes: 🛠 

All wireframes were designed and produced using [Balsamiq Mockups 3](https://balsamiq.com/). link to my [Wireframes](https://github.com/johndbigboi/The-Fitness-Lab/tree/master/wireframes). The Original design of the wireframe was altered as i focus on what is the best design for each django app.  

## Database Design: ⚙️

* During development of The LAB I worked with the standard <strong>sqlite3</strong>, database that comes installed with Django.
* In the production version of The LAB the database is a <strong>PostgreSQL</strong>, hosted and provided by Heroku.
* The The LAB development flowchart can be viewed [here](https://github.com/johndbigboi/The-Fitness-Lab/blob/master/wireframes/flowchart.png).
* I added Blog and Membership app which is not included in the flowchart.

#### The Blog Model:

The Post model within the Blog app holds the following data for the Blog post.

**Name**|**Key in db**|**Validation**|**Field Type**
:-----:|:-----:|:-----:|:-----:
User|user|null=True, on_delete=models.SET_NULL|ForeignKey
title|title|max\_length=200, default='some string'|CharField
creator|creator|max\_length=50,|CharField
content|content|NONE|TextField
created_date|created_date|auto_now_add=True|DateTimeField
published_date|published_date|blank=True, null=True, default=timezone.now|DateTimeField
views|views|default=0|IntegerField
image|image|upload_to='images', blank=True, null=True|ImageField

#### The Post Comment Model:

The Post Comment model within the blog app holds the following data for the every comments of the blog.

**Name**|**Key in db**|**Validation**|**Field Type**
:-----:|:-----:|:-----:|:-----:
post|post|related_name='postcomment', on_delete=models.CASCADE|ForeignKey
name|name|max\_length=200, , null=True|CharField
content|content|NONE|TextField
created_date|created_date|auto_now_add=True|DateTimeField


## Features: 🎡

### Features that have been developed:

* Register an account, login & logout functionality.
* Search by category by clicking navigation links.
* Users are able to check the item before it was purchased.
* Users are able to pay securely and get a confirmation email of the purchase.
* Users are able to create,edit and add comments on the blog.
* Users are able to choose membership option and can access their on profile page.

### Features that will be developed in the future:

* Users have personalised profile that they can edit and upload photos/avatars to.
* Nutrition tables for calories, carbohydrates and proteins.
* Users opt-in to subscribe to the mailing list for the latest information.
* Email authentication/duplicates for registry and security.
* User can rate and leave reviews for every product and services.
* Users access to workout programs and classes. 


## Technologies Used: 👨🏽‍💻

#### Languages: ⚙️

* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/)
* [JavaScript](https://www.w3schools.com/js/)
* [JSON](https://www.json.org/json-en.html)
* [Python](https://www.python.org/)

#### Tools & Libraries: ⚙️

* [Visual Studio Code](https://code.visualstudio.com/)
* [Django](https://www.djangoproject.com/)
* [Stripe](https://stripe.com/)
* [AWS](https://stripe.com/)
* [jQuery](https://jquery.com/)
* [Git](https://git-scm.com/)
* [Bootstrap 4.4](https://getbootstrap.com/)
* [Font-Awesome](https://fontawesome.com/icons?d=gallery)
* [TinyPng](https://tinypng.com/)

#### Databases:

* [SQlite3 - Development](https://www.sqlite.org/index.html)
* [PostgreSQL - Production](https://www.postgresql.org/)


## Planning and Testing: 📝

As I planned and developed this website using Python, SQlite3 and PostgreSQL database, I planned throughly and tested every line of the codes and made sure the codes were functioning properly, looking for errors and adjusting until the code ran without any issues. This process allowed me to learn more in depth on how to work codes with Python, SQlite3 and PostgreSQL database. 

### Feature Testing: 🎡 


<strong>Blog Post</strong>

* <strong>Plan: 📝</strong>  The user needs to register first to have full access and be able to submit, edit and leave commments. A guest user can only read the blogs.

* <strong>Implementation: 🏭</strong> Using a Post model which a registered member only can send blog post and able to edit.

* <strong>Test: 🧪</strong> To test this feature, I had to create several accounts in order to test the registration process as planned, checking the values were passed & stored in the database. Using the registered account, by logging in and out was found to be succesful.

* <strong>Result: 🏆</strong> The test passed as the created test user accounts are stored in the database with encrypted passwords and the user can login and log out of sessions without problems.

* <strong>Verdict: ✅</strong>  This test has passed based on the above criteria and notes.

<strong>Gym Membership</strong>

* <strong>Plan: 📝</strong>  The registered user can choose two type of membership and get the start and end date of the subscription

* <strong>Implementation: 🏭</strong>  To implement this feature, I needed to use the the request session in the database and save the choosen membership type for each member, and then save it in their profile page to view the start and end dates of the subscription. 

* <strong>Test: 🧪</strong>  To test this feature, I purchase the membership and choose a start and end date.

* <strong>Result: 🏆</strong>  The test passed for every purchased and subscribe made.

* <strong>Verdict: ✅</strong>  This test was passed based on the above criteria and notes.

<strong>Checkout using STRIPE</strong>

* <strong>Plan: 📝</strong> The User able to purchase a product from the shop e-commerce page. Handling sensitive information and keeping the privacy and integrity of the service within the legal guidelines. This feature needed to work seemlessly so that the user is informed as much as possible during the payment process.

* <strong>Implementation: 🏭</strong> To implement this feature, I use and follow the course material supplied by Code Institute aswell as the Django & stripe documentation. I created a model with Order and OrderItem pass it on the view.py and render to the template page. A validiation from STRIPE using stripe.js to process the payment succesfully.
* <strong>Test: 🧪</strong>  To test this feature, i created few purchases which i submitted and was successful.

* <strong>Result: 🏆</strong>  The test passed for every Purchase operation I carried out.

* <strong>Verdict: ✅</strong> This test was passed based on the above criteria and notes.

<strong>Profile Dashboard</strong>

* <strong>Plan: 📝</strong> A dashboard with all the needed information of the user, Information as order history, membership access and editable profile information.

* <strong>Implementation: 🏭</strong> To implement this feature, I created an account app which is connected as user to the Blog, Membership, and order history. All the user interactions was save in the database and can be pulled to be used in the account app and render in the profile dashboard page.

* <strong>Test: 🧪</strong>  To test this feature, I created few User and test every function of the website and view the profile information in the dashboard.

* <strong>Result: 🏆</strong> The test passed for every user operation I carried out.

* <strong>Verdict: ✅</strong> This test was passed based on the above criteria and notes.


### Validators and linters:

* The HTML code was validated with: [W3C](https://validator.w3.org/)
* The CSS code was validated with:[W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
* CSS Lint VSCode extension
* [PEP8](http://pep8online.com) and AUTOPEP8
* The website was tested on the following browsers:
    * Safari
    * Google Chrome
    * Mozilla Firefox
    * Internet Explorer

### Further testing:

I asked my family and friends for any issues they could find and what the page looked and felt like on their mobile and desktop devices. All the issues they found were fixed and tested again.


## Deployment: 🚀

The LAB was developed in Visual Studio Code, while Git and GitHub were used for version control and Heroku to host the repository.

### Deploying The LAB to Heroku:

### Running this project locally:

To run The LAB locally please follow the steps below!

Before starting make sure you have the following:

* An IDE (interactive development environment) such as <a href="https://code.visualstudio.com/">Visual Studio Code</a>.
* You <strong>MUST</strong> have the following installed on your machine>
* [Python3](https://www.python.org/)
* [Git](https://git-scm.com/)
* [PIP](https://pip.pypa.io/en/stable/installing/)
* You will <strong>need to</strong> create accounts with the following online services in order to run this project.
* [Heroku](https://www.heroku.com/)
* [AWS](https://aws.amazon.com/)
* [Stripe](https://stripe.com/)



## Instructions:

<em>WARNING: You may need to follow a different guide based on the OS you are using, read more <a href="https://python.readthedocs.io/en/latest/library/venv.html">here.</a></em>

1: <strong>Clone</strong> The-Fitness-Lab / The LAB repository by either downloading from [here](https://github.com/johndbigboi/The-Fitness-Lab) or type the following command into your terminal.
```bash
git clone https://github.com/johndbigboi/The-Fitness-Lab
```
2: <strong>Navigate</strong> to this folder in your terminal.
3: <strong>Enter</strong> the following command into your terminal.
```bash
python3 -m .venv venv
```
4: <strong>Initialize</strong> the environment by using the following command.
```bash
.venv\bin\activate
```

5: <strong>Install</strong> the requirements and dependancies from the requirements.txt file
```bash
pip3 -r requirements.txt
```

6: Within your IDE now <strong>create</strong> a file where you can store your secret information for the app, I used vscodes settings.json however you can just create an env.py file if you wish.

```bash
{
    "python.pythonPath": "/usr/local/bin/python3",
    "python.terminal.activateEnvironment": true,
    "python.linting.enabled": true,
    "files.autoSave": "onFocusChange",
    "files.useExperimentalFileWatcher": true,
    "terminal.integrated.env.osx": {
      "SECRET_KEY": "<your_secret_key_here>",
      "DEVELOPMENT": "1",
      "STRIPE_PUBLISHABLE": "<your_stripe_publishable_key_here>",
      "STRIPE_SECRET": "<your_stripe_secret_key_here>",
      "DATABASE_URL": "<your_database_url_here>",
}
```

7: <strong>Enter</strong> the following command into the terminal to migrate models into database.
```bash
python3 manage.py migrate
```

8: Then you need to <strong>Create</strong> a 'superuser' for the project using the terminal, enter the following command.
```bash
python3 manage.py createsuperuser
```

9: The app can now be ran locally using the following command.
```bash
python3 manage.py runserver
```

Congratulations, The LAB is now running locally on your machine! Happy Coding!

### Deploying The LAB to Heroku:

1: <strong>Create</strong> a requirements.txt file using the following command.
```bash
pip3 freeze > requirements.txt
```

2: <strong>Create</strong> a procfile with the following command.
```bash
echo web: python3 app.py > Procfile
```
3: Push these newly created files to your repository.
4: Create a new app for this project on the Heroku Dashboard.
5: Select your deployment method by clicking on the deployment method button and select GitHub.
6: On the dashboard, set the following config variables:

**Key**|**Value**
:-----:|:-----:
DATABASE\_URL|<your\_database\_url>
SECRET\_KEY|<your\_secret\_key>
STRIPE\_PUBLISHABLE|<your\_stripe\_publishable\_key>
STRIPE\_SECRET|<your\_stripe\_secret\_key>

* 7: <strong>Click</strong> the deploy button on the heroku Dashboard.
* 8: Wait for the build to finish and click the view project link once it has!

Congratulations, The LAB is now hosted on Heroku and is live!



## Bugs: 🐞

#### Bugs During Development: 


Developing this project while being new to Python Django, I encountered errors along the way that proved to be somewhat challenging and it took me 
longer to find solutions and fixes.

<strong>Editing Blog</strong>

* <strong>Bug:</strong> 🐞 During Development i had an issue in the url pk=post.id as hard time getting the POST data from the form.
 
* <strong>Fix:</strong> 🛠 As I'm new in using Django, After a lot of research, i had a mix up in the urls and views as i used blog.id. To fix it i read the view code line by one to where i had a mistake and found i used blog.id not post.id. 
* <strong>Verdict:</strong> ✅ This bug was squashed and I could continue working on other aspects of the project.


## Credits: 💳

* I used [Stack Overflow](https://stackoverflow.com/) for guides in developing my own codes.
* Image for README.md multi device layouts taken from [techsini](https://techsini.com/multi-mockup/index.php)
* Image editor online [pixlr](https://pixlr.com/) and [imgonline](https://www.imgonline.com.ua/)
* Used to make favicon [Favicon Generator](https://www.favicon-generator.org/) 
* Used for color theme [color-hex.com](https://color-hex.com/)
* Helps my project for height and width [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB)
* Big Thanks to Code Institute Tutors na my two mentor Mr. Simen Daehlin and Brian Macharia
* [freepik](http://www.freepik.com) images design by Daniel Apodaca, CREATIVEART, AND FREEPIK 


## Disclaimer:📃

The LAB is developed for educational purposes only, and is not intended for use in any other capacity.

[Back to top ↑](#muscle-farm)

