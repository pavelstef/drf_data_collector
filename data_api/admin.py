""" Registration of the model in the admin panel """

from django.contrib import admin
from data_api.models import Greeting

admin.site.register(Greeting)
