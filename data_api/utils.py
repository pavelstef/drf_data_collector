"""
Utils for getting and normalizing data from an external source.
As well as adding this data to the database.
"""

import datetime
import locale
import requests
from json.decoder import JSONDecodeError

from django.conf import settings

from data_api.forms import GreetingForm


def get_data(url=settings.DATA_SOURCE_URL) -> dict:
    """ Getting data from an external source """
    try:
        raw_data = requests.get(url=url).json()
    except requests.exceptions.RequestException:
        return {'error': 'The external source is unreachable.'}
    except JSONDecodeError:
        return {'error': 'The data could not be decoded as JSON.'}

    return raw_data


def normalize_russain_date(value: str, template='%d %B %Y года') -> datetime:
    """ Normalize date from string in Russian format to class format 'datetime.datetime' """
    locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
    date_time = datetime.datetime.strptime(value, template)
    return date_time.date()


def normalize_iso_date(value: str, template='%Y-%m-%d') -> datetime:
    """ Normalize date from string in ISO format to class format 'datetime.datetime' """
    date_time = datetime.datetime.strptime(value, template)
    return date_time.date()


def create_records(raw_data_dict: dict) -> dict:
    """
    We will create objects in the database through the form and will do validation.
    It's a little resource intensive, but safe.
    """
    if raw_data_dict:
        data_rows_got = raw_data_dict.get('total')
        data_rows_created = 0
        data_rows_errors = []
        for row in raw_data_dict['items']:
            content_dict = {
                'id': int(row.get('id')),
                'category': row.get('category'),
                'from_row': row.get('from'),
                'title': row.get('title'),
                'text': row.get('text'),
                'thedate': normalize_russain_date(row.get('thedate')),
            }
            greeting_form = GreetingForm(content_dict)

            if greeting_form.is_valid():
                greeting_form.save()
                data_rows_created += 1
            else:
                data_rows_errors.append({content_dict.get('id'): greeting_form.errors})

        message = {
            'got_rows': data_rows_got,
            'created_rows': data_rows_created,
            'errors': data_rows_errors
        }
        return message
