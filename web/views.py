from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from django.db.models.query import QuerySet
from django.http import response
from rest_framework.views import APIView
from itertools import groupby
from .models import Menu, Order
from rest_framework import viewsets
from rest_framework import permissions
from web.serializers import MenuSerializer, OrderSerializer, UserSerializer

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import MyTokenObtainPairSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class MenuViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows menus to be viewed or edited.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAdminUser]


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAdminUser]


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
