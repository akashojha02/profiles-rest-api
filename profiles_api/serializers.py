from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """ Serializers is a name field to test our Api"""

    name = serializers.CharField(max_length=10)
