""" Tests of data_api.views """

import os
import json

from rest_framework.test import APITestCase

from data_api.models import Greeting
from data_api.utils import create_records


class DataManagementViewTests(APITestCase):
    """ Tests of the DataManagementView """

    @classmethod
    def setUpTestData(cls):
        file_patch = os.path.join(os.path.dirname(__file__), 'data.mock')
        with open(file_patch, 'r', encoding='UTF-8') as file:
            test_data_dict = json.load(file)
        _ = create_records(test_data_dict)

    def test_get_method(self) -> None:
        response = self.client.get(path='/api/v1/management')
        self.assertEqual(response.status_code, 200)

        queryset = Greeting.objects.all()
        self.assertJSONEqual(str(response.content, encoding='utf8'), {"count": len(queryset)})


class GreetingJSONViewTests(APITestCase):
    """ Tests of the GreetingJSONView"""

    content = {
        "count": 1,
        "greetings": {
            "id": 52,
            "category": "greetings",
            "from_row": "Д. Медведев",
            "title": "Н.И.Пастухову",
            "thedate": "2008-05-13"
        }
    }

    @classmethod
    def setUpTestData(cls):
        file_patch = os.path.join(os.path.dirname(__file__), 'data.mock')
        with open(file_patch, 'r', encoding='UTF-8') as file:
            test_data_dict = json.load(file)
        _ = create_records(test_data_dict)

    def test_retrieve_by_id(self) -> None:
        response = self.client.get(path='/api/v1/json/greetings/52')
        self.assertEqual(response.status_code, 200)

        content = json.loads(response.content)
        self.assertEqual(content['count'], self.content['count'])
        self.assertEqual(content['greetings']['id'], self.content['greetings']['id'])
        self.assertEqual(content['greetings']['title'], self.content['greetings']['title'])
        self.assertEqual(content['greetings']['thedate'], self.content['greetings']['thedate'])

    def test_retrieve_by_date(self) -> None:
        response = self.client.get(path='/api/v1/json/greetings/2008-05-13')
        self.assertEqual(response.status_code, 200)

        content = json.loads(response.content)
        self.assertEqual(content['count'], self.content['count'])
        self.assertEqual(content['greetings'][0]['id'], self.content['greetings']['id'])
        self.assertEqual(content['greetings'][0]['title'], self.content['greetings']['title'])
        self.assertEqual(content['greetings'][0]['thedate'], self.content['greetings']['thedate'])
