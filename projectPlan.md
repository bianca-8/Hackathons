Memento Spark Documentation
===========================

Introduction:
-------------

We built a web app that stores memories in the form of Memento Posts. 2 types of users will be able to use the app; admin & user. It has a basic CRUD functionality with adding/updating/retrieving/deleting posts. Also, users can be registered and authenticated using Django authentication. We have mini features like creating a polaroid, applying random filters to it, and will be able to download it.

Project Overview:
-----------------

Talking about key features, we have various features in this initial version, these are the highlight features:

1.  A user can upload their profile picture which is stored as ImageField in the database(sqlite).

2.  Polaroid Generator

3.  Random Filters Implementation on Polaroid.

4.  Mementos(Posts) can be created, edited, retrieved, and deleted with the help of a primary key.

5.  A user can have different Mementos.

6.  Users can see how old the mementos was, can store up to 3 images as a memory, and also add a single sound to a memento.

7.  Email Automation using SMTP, when a user deletes any memento, they will receive an email.

Technology Stack:
-----------------

For the front end, we used HTML, CSS(SCSS), JavaScript, and Jquery with Bootstrap. For the backend, we are using the latest version of Django and for these environmental variables you can create .env file in the root directory and store your keys and everything and pass it to settings.py file.

Settings.py file:
================

EMAIL_BACKEND  =  os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')

EMAIL_HOST  =  os.environ.get('EMAIL_HOST', 'smtp.gmail.com')

EMAIL_USE_TLS  =  os.environ.get('EMAIL_USE_TLS', True)

EMAIL_PORT  =  os.environ.get('EMAIL_PORT', 587)

EMAIL_HOST_USER  =  os.environ.get('EMAIL_HOST_USER', '')

EMAIL_HOST_PASSWORD  =  os.environ.get('EMAIL_HOST_PASSWORD', '')

LOGIN_URL  =  os.environ.get('LOGIN_URL', 'login')

.env file:
==========

.env

EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend

EMAIL_HOST=smtp.gmail.com

EMAIL_USE_TLS=True

EMAIL_PORT=587

EMAIL_HOST_USER=your_host_email

EMAIL_HOST_PASSWORD=your_pwd

Tech stacks:
------------

Frontend: HTML, CSS, JS, JQuery, Bootstrap

Backend: Django

Database: Sqlite.

User Flows:

1.  User Registration

2.  User Login

3.  Home Page where user can see all their mementos.

4.  Can Edit or Delete

5.  My Mementos Page is where they can see the mementos info along with a Polaroid generator.

6.  Can Download the generated Polaroid.

7.  User Profile page, where user info is stored, and can log in.

8.  Whenever a User Deletes some mementos, they will get an email saying it is deleted.

9.  Users can logout and be redirected to the login page again.