"""  Serializers for the or the data_api module """


from rest_framework import serializers

from data_api.models import Greeting


class GreetingSerializer(serializers.ModelSerializer):
    """ A Serializer for model Greeting """
    class Meta:
        model = Greeting
        fields = ('__all__')
