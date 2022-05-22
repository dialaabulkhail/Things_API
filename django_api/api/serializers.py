
from rest_framework import serializers
from django_api.models import Thing


# it allows the data to be exposed to JSON
# sending data to database -> serializers will check if data matches the model
class ThingSerilizer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'description')
        model = Thing
