from django.contrib.auth.models import User
from django.db.models import fields
from .models import Menu, Order
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class MenuSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = ['id', 'food_name', 'date', 'amount', 'users']

    def get_users(self, obj):
        users = User.objects.filter(pk__in=obj.order_set.all().values('user'))
        return UserSerializer(users, many=True).data


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    menu = MenuSerializer()
    class Meta:
        model = Order
        fields = ['id', 'menu']


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token       