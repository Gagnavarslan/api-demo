# CoreWaves - CoreData API demo project
A Demo project to query the [CoreData](http://www.azazo.com/coredata/) API.

> CoreData ECM is a SaaS (software as a service) subscription software package
> that is based on a modern approach to the management of all information and
> projects for companies and public bodies.

## Getting started
### Prerequisites
This project is a [Django 1.8](https://www.djangoproject.com/) app, intended to
be a boilerplate for projects that use the CoreData API. In order to use this
app credentials to a working CoreData instance is required.

The setup instructions assume the following;

- Linux/MacOS terminal or [Git bash](https://git-scm.com/downloads) on Windows
- Git
- Python (2.6+) and [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) 
- Credentials and info for a running CoreData
    - Configurable in the .env file

### Up and running
In your environment do the following:

1. Grab af copy of the code

    ```sh
    git clone https://github.com/Gagnavarslan/api-demo
    ```
2. Create a virtual environment

    ```sh
    cd api-demo
    virtualenv . -—no-site-packages
    source bin/activate
    bin/pip install -r requirements/local.txt
    ```
3. Edit the `.env` file (add the password):

    ```sh
    COREDATA_URL=https://airwaves.coredata.is/
    COREDATA_USER=api-demo
    COREDATA_PASSWORD=ENTER-PASSWORD # <- Here
    ```
4. Prepare app, and start it:

    ```sh
    python manage.py migrate
    python manage.py runserver
    ```

### What are you looking at?
When you look at the running app,
[http://localhost:8000/](http://localhost:8000/), you will see a tab
"Contacts". Under this page you will see a simple list of the 20 first contacts
found on the CoreData server (as defined in the COREDATA_URL in the .env file).

This is a very bare-bone django app that just fetches from a restful api and
displays the found items as a list on a simple view.

To explore the API and what it has to offer, you can log into CoreData using
the same credentials as you should have obtained and navigate the api's live
Swagger documentation:
[airwaves.coredata.is/api/v2/doc/](https://airwaves.coredata.is/api/v2/doc/)
