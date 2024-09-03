# Task-1
- Created a Virtual Environment: DjangoAssignment
- Activated venv
- installed Django in venv
- created login_system project
- created loginify app inside the project
- registered loginigy app in settings.py

# Task-2
- Created views -> testDemo in loginify app to check configs
- returned HTTPresponse -> Hello World
- registered views in app>urls.py
- registered urls in project>urls.py 
- Properly configured URL mapping and other configs

# Task-3

- adding templetes
- added UserDetails class in models.py and stagged the changes using cmd -> python manage.py makemigrations
- migrate to DB using -> python manage.py migrate 
- Cerated serializers.py file to manage api objects.
- setting up signup page and login page in views.py -> loginigy
- added url to urls.py file in loginify app
- craeted signup form in loginify app using Django form
- implemented -> on successful signup redirecting to login page

# Task-4

- Created superUser using -> python manage.py createsuperuser.
- Verified the superuser endpoint by visiting the admin interface.
- created new user instance.
- Retrived all user information.
- Retrieved single user information by name
- deleted user using username.


# Task-5

- Get all user details view: Retrieves and displays details of all users. -> /userList
- Get Single user using pk -> singleUser/<id>
- Change feilds using pk -> PUT method singleUser/<id> with changed Json in body
- deleted user using email