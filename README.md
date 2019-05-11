# Item Catalog

Item Catalog is an application that provides a list of items within a variety of categories. It also provides a user registration and authentication system using Google Accounts. Registered users have the ability to post, edit and delete their own items.

## Application Set Up

1. Clone or download the repository

2. In order to initialise the database navigate to the root folder and run:
```python database_setup.py```

3. Run: ```python catalog.py```

4. Navigate to localhost:5000 in your browser

5. In order to get the Google logins working you will have to set up and account at Google API Console and provide a google secret and api key for OAuth2 authentication. Replace the client_secrets.json with your client secret and also replace the client_id value in login.js on line 6.

## Setting up Google Authentication

1. Create an app project in the Google APIs Console — https://console.developers.google.com/apis

2. Go to your app's page in the Google APIs Console

3. Choose Credentials from the menu on the left.

4. Create an OAuth Client ID.

5. When you're presented with a list of application types, choose Web application.

6. You can then set the authorized JavaScript origins (if you're using localhost, set this to http://localhost:5000, redirect should have http://localhost:5000/postmessage, if you're using a different domain change localhost:5000 with your domain)

7. You will then be able to get the client ID and client secret, there is a button to download the client secret json as well.

8. Replace the client_secrets.json with your client secret and also replace the client_id value in login.js on line 6.

## How to use the application

In order to use the application, user has to first click the login link in the top right corner.
This will navigate the user to a login page which contains a button for login with Google account.

If this is the first time that the user is logging in, a user account for item catalog will be automatically created.

After logging in user can use the plus icons on catalog and item page to add new categories and items as well as edit and delete any existing categories and items they created.

Users are not allowed to add, edit and delete items from other users' categories and neither can they remove or edit these categories.

Not logged in users are only allowed to browse the catalog.

## Supported browsers

Only tested on Chrome, should run on Safari and other webkit browsers.

## Dependencies

* SQLAlchemy
* Jquery
* Flask
* python

## Resources used

Udacity Full Stack Nanodegree Course
