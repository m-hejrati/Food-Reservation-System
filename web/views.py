from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from django.db.models.query import QuerySet
from django.http import response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from itertools import groupby
from .models import Menu, Order
from rest_framework import viewsets
from rest_framework import permissions
from web.serializers import MenuSerializer, OrderSerializer, UserSerializer

from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenViewBase
from rest_framework.permissions import AllowAny, IsAdminUser
from .serializers import MyTokenObtainPairSerializer

from json import JSONEncoder
from datetime import datetime

from django.core import serializers
from django.contrib.auth.middleware import get_user

from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db.models import Sum, Count
from django.http import JsonResponse
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.http import require_POST
from rest_framework.authtoken.models import Token


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


@csrf_exempt
@require_POST
def reserve(request):

    entered_menu_id = request.POST['menu_id']
    entered_user_id = request.POST['user_id']

    entered_user = User.objects.get(id=entered_user_id)
    entered_menu = Menu.objects.get(id=entered_menu_id)

    real_user = request.user
    # TODO: debug AnonymousUser  

    if request.user.is_authenticated:
  
        if (real_user == IsAdminUser) or (real_user.id == entered_user_id):
            
            Order.objects.create(user=entered_user, menu=entered_menu)
            
            return JsonResponse({ 
                'Success': 'True',
                }, encoder=JSONEncoder)

        else:
            
            return JsonResponse({
                'Success': 'False',
                'Message': 'You are not allowed to order for another user ...',
                }, encoder=JSONEncoder)

    else:
        return JsonResponse({
            'Success': 'False',
            'Message': 'You are not authenticated ...',
            }, encoder=JSONEncoder)


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
