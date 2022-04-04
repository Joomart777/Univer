from django.shortcuts import render


# Create your views here.

from rest_framework.generics import *

from univer_app.models import *
from univer_app.serializers import ProductSerializer


class ListCreateView(ListCreateAPIView):
    queryset = Univer.objects.all()
    serializer_class = ProductSerializer

class DeleteUpdateRetrieveView(RetrieveUpdateDestroyAPIView):
    queryset = Univer.objects.all()
    serializer_class = ProductSerializer