from django.contrib.auth.models import User
from .models import Menu, Order
from rest_framework import viewsets
from rest_framework import permissions
from web.serializers import MenuSerializer, OrderSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class MenuViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows menus to be viewed or edited.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
