""" Tests of data_api.utils """

import datetime
import os
import json

from django.test import SimpleTestCase, TestCase

from data_api.utils import normalize_russain_date, normalize_iso_date, create_records
from data_api.models import Greeting


class ApiUtilsDateNormalizeTests(SimpleTestCase):
    """ Tests of normalize methods """

    def test_normalize_russain_date(self) -> None:
        self.assertEqual(normalize_russain_date("16 августа 2013 года"), datetime.date(2013, 8, 16))
        self.assertEqual(normalize_russain_date("25 июня 2009 года"), datetime.date(2009, 6, 25))

    def test_normalize_iso_date(self) -> None:
        self.assertEqual(normalize_iso_date("2013-8-16"), datetime.date(2013, 8, 16))
        self.assertEqual(normalize_iso_date("2009-6-25"), datetime.date(2009, 6, 25))


class ApiUtilsCreateRecordsTests(TestCase):
    """ A test of the create_records method """

    def test_create_records(self) -> None:
        file_patch = os.path.join(os.path.dirname(__file__), 'data.mock')
        with open(file_patch, 'r', encoding='UTF-8') as file:
            test_data_dict = json.load(file)
        self.assertEqual(test_data_dict.get('total'), 7)

        message = create_records(test_data_dict)
        self.assertEqual(message.get('got_rows'), 7)
        self.assertEqual(message.get('created_rows'), 6)
        self.assertEqual(message.get('errors'),
                         [{52: {'id': ['Поздравление с таким Id уже существует.']}}])

        queryset = Greeting.objects.filter(id=19040)
        self.assertEqual(queryset[0].id, int(test_data_dict['items'][0]['id']))
        self.assertEqual(queryset[0].category, test_data_dict['items'][0]['category'])
        self.assertEqual(queryset[0].from_row, test_data_dict['items'][0]['from'])
        self.assertEqual(queryset[0].title, test_data_dict['items'][0]['title'])
        self.assertEqual(queryset[0].text, test_data_dict['items'][0]['text'])
