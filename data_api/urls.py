""" data_api URLs Configuration """

from django.urls import path
from rest_framework.documentation import include_docs_urls

from data_api import views

urlpatterns = [
    path('api/v1/management', views.DataManagementView.as_view(), name='api_data_management'),

    path('api/v1/json/greetings', views.GreetingJSONView.as_view({'get': 'list'}),
         name='api_json_greetings_list'),
    path('api/v1/json/greetings/<attribute>', views.GreetingJSONView.as_view({'get': 'retrieve'}),
         name='api_json_greetings_retrieve'),

    path('api/v1/xlsx/greetings', views.GreetingXLSXView.as_view({'get': 'list'}),
         name='api_xlsx_greetings_list'),
    path('api/v1/xlsx/greetings/<attribute>', views.GreetingXLSXView.as_view({'get': 'retrieve'}),
         name='api_xlsx_greetings_retrieve'),

    path('api/v1/docs', include_docs_urls(title='API of the data collection app'))
]
