from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Menu, Order

admin.site.site_header = "Food Reservation Admin"

admin.site.register(Menu)
admin.site.register(Order)

admin.site.unregister(Group)