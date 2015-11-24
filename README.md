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

If this is your first encounter with Django, now would be a good time to read
up a bit. Here are a few links to get you started:

- [Offical Django getting started guide](https://www.djangoproject.com/start/)
- [Starting a Django Project](https://realpython.com/learn/start-django/)
- [Django for beginners  - video](https://www.youtube.com/watch?v=zTNA0MtZwso)

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

### How does this app work?
Under the `airwaves` folder there is an app folder, `contacts`. This is where
everything happens. In the `urls.py` file we make sure that when you navigate
to [locahost:8000/contacts](localhost:8000/contacts) Django will match your
request to the view defined in `views.py`.

```python
urlpatterns = [
    # `^$` matches `contacts/`
    url(r'^$', views.Contacts.as_view(), name='list'),
]
```

The view (`Contacts` class), uses a template (stored under the `templates`
folder. It gets the context (list of contacts) by querying the CoreData API
from the CoreData instance defined in the `.env` file. This is fetched by
using the Python requests library (basic auth). The request is made, and the
returned items are injected into the context and returned to the template.

```python
class Contacts(TemplateView):
    template_name = "contacts/contacts_list.html"

    def get_context_data(self, **kwargs):
        context = super(Contacts, self).get_context_data(**kwargs)

        # Send a request to the CoreData API
        # JSON is returned
        contacts = requests.get(
            '{}api/v2/contacts'.format(COREDATA_URL),
            auth=(COREDATA_USER, COREDATA_PASSWORD)
        )
        context["contacts"] = contacts.json()

        return context
```

The template then loops through the items to display a list of the found first
20 contacts.

```html
    <div class="list-group">
        {% for contact in contacts.objects %}
          <a href="#" class="list-group-item">
            <h4 class="list-group-item-heading">{{ contact.title }}</h4>
          </a>
        {% endfor %}

    </div>
```
