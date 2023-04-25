# Django-Skeleton #

A Django project starter template intentionally preconfigured with "bare bones" functionality.

**Current Django Version:** &nbsp;Django 4.2

Deployed on [Heroku](https://dj-skel.herokuapp.com/)

### Disclaimers: ###
This project makes no claim to be the "best way" to set up a Django project.

## Functionality & Configuration ##
The project has been set up with the following functionality/configuration:
- Code Formatting / Styling
     - Python
          - black
          - flake8 (79 character per line ignored)
          - isort
     - All code formatting packages installed as Pipenv [dev-packages]
- Database
     - Datebase:  PostgreSQL
     - Database Adapter/Connector:  psycopg2
- Deployment
     - Configured for Heroku (with Procfile and runtime.txt)
- Docker - Not currently set up for Docker
- Email
     - Configured by environment as follows:
          - DEV:  To console (EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend')
          - TEST:  To localmem (EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend')
          - PROD: SMTP (EMAIL_BACKEND = django.core.mail.backends.smtp.EmailBackend)  
     - Specific values for settings read from environment.
     - Alternate configurations commented out in code for quick changes while debugging.  
- Environments / Environment Variables 
     - Separate environments for local development (DEV), test (TEST), and production (PROD)
     - Variable named 'DEV' assigned in environment specifies the environment.  Possible values:  DEV, TEST, PROD
     - Where are variables stored?
          - DEV:    .env file (not included).  Variables read into environment by Pipenv.
          - TEST:   .env-test file (not included).  Variables read into environment by pytest-dotenv.
          - PROD:   Configured through Heroku settings.  Variables read into environment by Heroku.  
     - See included EXAMPLE.env for example .env file. 
- Front End Frameworks:
     - CSS:  None
     - JavaScript:  None
- Project/App Structure
     - Project
          - 'config' folder with settings.py, wsgi.py, asgi.py, and project-level urls.py.
     - Apps
          - 'main' app placeholder
               - Can be used or scrapped.
          - 'accounts' app for user management
- Source Control / Repository
     - git (includes .gitignore)
     - [GitHub Repo](https://github.com/fiofury1/django-skeleton)
- Static Files
     - Configured to use WhiteNoise for both development and production.
     - During development, configured to look for static files in 'static/' folder in root of project and apps.
     - Set up to collect static files into 'staticfiles/' folder in project root.
          - Note that 'staticfiles/' directory not included in source control so 'collect static' command will need to be run to include them in desired environment.
     - Static files compressed and cached
       (STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage')
       *See whitenoise documentation for non-cached option.* 
- Testing
     - Uses pytest / pytest-django packages.
          - pytest settings found in pytest.ini.
          - Uses conftest.py files to define test data/fixtures.
               - Includes global conftest.py in project root
                    - Many useful fixtures predefined and used
               - Includes placeholder conftest.py files in project level testing folder, 'main' app, and 'account' app.
          - Uses 'mixer' (package) for generating test data.
     - Uses pytest-dotenv to read environment variables into TEST environment.
     - Uses Selenium and ChromeDriver for functional/integration testing.  
          - Does not include a ChromeDriver in source code.  You will need to install ChromeDriver into your environment(s).
     - Includes pytest-cov (i.e. "Coverage").  
          - Provided .coveragerc file includes files/folders to ignore from coverage report.
          - 100% Coverage  
     - Test file/folder structure
          - Project level tests to be included in the project level 'tests' folder
          (i.e. '<project_name>/tests/').  
               - Includes example test file and template for functional tests. 
          - App level tests intended to be stored in app level 'tests' folder.
          (i.e. '<project_name>/<app_nam>/tests/').  This structure has been implemented in the provided 'main' app.
               - Includes example test file, working functional tests file, and template files for testing models, templates, urls, and views.
     - All testing packages installed as Pipenv [dev-packages]
- User Management
     - CustomUser Model
          - Set up in 'accounts' app
          - Extends 'AbstractUser' with no additional fields added.
     - Implemented using Django included 'auth' app.
     - URLs/Views not included by 'auth' (i.e. Sign-up) included in 'accounts/' app.
     - Functionality implemented:
          - Sign-up (no email confirm)
          - Login
          - Logout
          - Password Reset (with confirm email)
          - Password Change
     - HTML and email templates added to project level 'templates/registration/' folder.
     - Includes functional/Selenium tests of all user  management functions.
- Virtual Environment
     - Pipenv
     - Environment variables loaded from .env by Pipenv in DEV. 
- Web Server
     - Django Dev Server used by default for DEV and TEST.
     - Gunicorn for PROD.
- Other Packages
     - django-debug-toolbar
     - django-extensions
- Misc/Other
     - Time Zone as 'America/New York'


## Forking or Cloning ##
After forking or cloning the project, you will need to:

The following does not cover:
-  Editor/IDE specific setup (ex. create project/workspace in your editor/IDE)
-  Instructions for setting up the repo/remote with git/GitHub.
-  Tweaks related to using SQLite.

1.  Create a new virtual environment and install dependencies using Pipenv.  
     - This should be done from the root folder of the project.  
     - The Python version used for your virtual environment needs to match the version in the Pipfile.
     - The `install` command will both create the virtual environment and install your dependencies.
          - **WARNING:**  Using `pipenv install` will install dependencies ***from the Pipfile***.  The Pipfile in this project does not currently specify versions of packages, which means the latest version will be installed.  To create a deterministic build of the project, then use `pipenv sync` instead.  This will result in packages being installed as specified in the Pipfile.lock file.
          - Use `$ pipenv install` to install non-dev dependencies.  
          - Use `$ pipenv install --dev` to install all dependencies including dev dependencies. 
2.  In PostgreSQL, set up PostgreSQL user for project and local Postgres database.
3.  Create an .env file in project root (or load environment variables in another way).  If using .env file, see EXAMPLE.env for example .env file.
4.  Update Database variables in .env to local Postgres.
5.  Create Django Admin superuser.
6.  Update Django Admin URL (for security) (in project urls.py).
7.  Update Time Zone as needed (in settings.py).
8.  Update Email Settings (in .env).
9.  Update Allowed Hosts (in settings.py).
10.  Add 'staticfiles' directory in root of project (or run `$ python manage.py collectstatic` and directory will be created)
11.  Customize:
     - Project level README.md to describe project.
     - Home Page Title and Heading.  Obviously, also delete the header about Django-Skeleton.

## Updating Django and Other Dependencies (SECTION UNDER CONSTRUCTION) ##
Since Django has a regular release cycle, I use new Django releases as a trigger to update Django and all other project dependencies. 

Note per [Django documentation](https://docs.djangoproject.com/en/4.1/howto/upgrade-version/#required-reading):
> If you’re upgrading through more than one feature version (e.g. 2.0 to 2.2), 
it’s usually easier to upgrade through each feature release incrementally (2.0 to 2.1 to 2.2) 
rather than to make all the changes for each feature release at once. For each feature release, 
use the latest patch release (e.g. for 2.1, use 2.1.15).

To update:
- Recommend first resolving any depreciation warning messages issued when running test suite in pytest. 
     - Look into django-upgrade package. https://github.com/adamchainz/django-upgrade
     - Note that when running the local development server can use the following to view warnings:
          - `$ python -Wd manage.py runserver` to view deprecation warnings.
          - `$ python -Wa manage.py runserver` to view all warnings.
- Update all packages/dependencies.
     (Hints:  
     - Use `$ pipenv update --outdated` to see which packages are out of date
     - Use `$ pipenv update <package_name>` to update a specific package
- Update 'Current Django Version' in settings.py