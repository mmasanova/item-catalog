# Item Catalog

Item Catalog is an application that provides a list of items within a variety of categories. It also provides a user registration and authentication system using Google Accounts. Registered users have the ability to post, edit and delete their own items.

## Application Set Up

1. Clone or download the repository

2. In order to initialise the database navigate to the root folder and run:
```python database_setup.py```

3. Run: ```python catalog.py```

4. Navigate to localhost:5000 in your browser

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