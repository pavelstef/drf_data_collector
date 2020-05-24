""" Views of API interface for the data_api module """

from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import Http404

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from drf_renderer_xlsx.mixins import XLSXFileMixin
from drf_renderer_xlsx.renderers import XLSXRenderer

from data_api.models import Greeting
from data_api.serializers import GreetingSerializer
from data_api.utils import get_data, create_records, normalize_iso_date


class DataManagementView(APIView):
    """ A View data management """

    model = Greeting

    def get(self, request):
        """ GET Method.  Getting information about the number of records in the database """
        context = {
            'count': len(self.model.objects.all()),
        }
        return Response(context)

    def post(self, request):
        """ POST Method.  Refreshing data from an external source and creating records in the DB """
        raw_data = get_data()
        if 'error' in raw_data.keys():
            context = raw_data
        else:
            message = create_records(raw_data)
            context = {
                'message': message
            }

        return Response(context)


class GreetingJSONView(ListModelMixin, viewsets.GenericViewSet):
    """ A View to get data in JSON format """

    queryset = Greeting.objects.all()
    serializer_class = GreetingSerializer

    # A customized retrieve method
    def retrieve(self, request, attribute=None):
        """
        GET Method.
        Getting the specific greetings from the DB.
        Greetings can be filtered by id or by date.
        """

        if attribute.isdigit():
            greetings = get_object_or_404(self.queryset, id=attribute)
            serializer = self.serializer_class(greetings)
            count = 1
        else:
            try:
                attribute = normalize_iso_date(attribute)
            except ValueError:
                raise Http404

            greetings = get_list_or_404(self.queryset, thedate=attribute)
            serializer = self.serializer_class(greetings, many=True)
            count = len(greetings)

        return Response({'count': count, 'greetings': serializer.data})


class GreetingXLSXView(XLSXFileMixin, ListModelMixin, viewsets.GenericViewSet):
    """ A View to get data in XLSX format """

    queryset = Greeting.objects.all()
    serializer_class = GreetingSerializer
    renderer_classes = [XLSXRenderer]
    filename = 'Greetings.xlsx'

    # A customized retrieve method
    def retrieve(self, request, attribute=None):
        """
        GET Method.
        Getting the specific greetings from the DB.
        Greetings can be filtered by id, by date.
        """

        if attribute.isdigit():
            greetings = get_object_or_404(self.queryset, id=attribute)
            serializer = self.serializer_class(greetings)
        else:
            try:
                attribute = normalize_iso_date(attribute)
            except ValueError:
                raise Http404

            greetings = get_list_or_404(self.queryset, thedate=attribute)
            serializer = self.serializer_class(greetings, many=True)

        return Response(serializer.data)
