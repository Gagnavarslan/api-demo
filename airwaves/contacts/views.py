import requests

from django.shortcuts import render
from django.views.generic import TemplateView


class Contacts(TemplateView):
    template_name = "contacts/contacts_list.html"

    def get_context_data(self, **kwargs):
        context = super(Contacts, self).get_context_data(**kwargs)

        contacts = requests.get(
            'https://airwaves.coredata.is/api/v2/contacts',
            auth=('Administrator', 'Administrator')
        )
        context["contacts"] = contacts.json()

        return context
