from django.db import models
from django.contrib.auth.models import User


class Menu(models.Model):
    food_name = models.CharField(max_length=64)
    date = models.DateField()
    amount = models.IntegerField()

    def __str__(self):
        return "{}, {}".format(self.date, self.food_name)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return "{}, {}".format(self.user, self.menu)