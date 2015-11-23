import os
import requests

from django.views.generic import TemplateView


COREDATA_URL = os.environ.get("COREDATA_URL")
COREDATA_USER = os.environ.get("COREDATA_USER")
COREDATA_PASSWORD = os.environ.get("COREDATA_PASSWORD")


class Contacts(TemplateView):
    template_name = "contacts/contacts_list.html"

    def get_context_data(self, **kwargs):
        context = super(Contacts, self).get_context_data(**kwargs)

        contacts = requests.get(
            '{}api/v2/contacts'.format(COREDATA_URL),
            auth=(COREDATA_USER, COREDATA_PASSWORD)
        )
        context["contacts"] = contacts.json()

        return context
