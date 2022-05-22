from rest_framework import generics
from .serializers import ThingSerilizer
from django_api.models import Thing

class ThingsListAPIView(generics.ListAPIView):
    # specify the query set
    queryset = Thing.objects.all()
    serializer_class = ThingSerilizer

class ThingsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerilizer