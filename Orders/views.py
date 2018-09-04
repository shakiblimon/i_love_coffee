from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_auth.serializers import JWTSerializer
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework import generics
from . import models
from . import serializers

from rest_framework_jwt.views import ObtainJSONWebToken

from .serializers import JWTSerializer


class OrderList(generics.ListCreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class OrderDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class ViewHistory(generics.ListAPIView):
    queryset = models.ViewDetails.objects.all()
    serializer_class = serializers.ViewHistorySerializer


class ObtainJWTView(ObtainJSONWebToken):
    serializer_class = JWTSerializer