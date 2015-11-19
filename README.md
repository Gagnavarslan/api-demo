# CoreWaves - CoreData API demo project
A Demo project to query the [CoreData](http://www.azazo.com/coredata/) API.

> CoreData ECM is a SaaS (software as a service) subscription software package
> that is based on a modern approach to the management of all information and
> projects for companies and public bodies.

## Getting started
### Prerequisites
This project is a [Django 1.8](https://www.djangoproject.com/) app, inteded to be a
boiler plate for projects that use the CoreData API. In order to use this app
credentials to a working CoreData instance is required.

The setup instructions assume the following;

- Linux/MacOS terminal or [Git bash](https://git-scm.com/downloads) on Windows
- Git
- Python (2.6+) and [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) 
- Credentials and info for a running CoreData

```
git clone https://github.com/Gagnavarslan/api-demo

cd api-demo
virtualenv . -—no-site-packages
source bin/activate
bin/pip install -r requirements/local.txt

python manage.py migrate

python manage.py runserver
```
