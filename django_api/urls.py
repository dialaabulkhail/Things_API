from django.urls import path
from django_api.api.viewset import (
                                    ThingsListAPIView,
                                    ThingsDetailAPIView
                                    )

urlpatterns = [
    path('api/vl/things-list', ThingsListAPIView.as_view(), name='things_list'),
    path('api/vl/<int:pk>', ThingsDetailAPIView.as_view(), name='thing_detail')

]
