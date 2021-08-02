from django.db import models
from django.contrib.auth.models import User

from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  

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


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)
    email_plaintext_message += "\nsend this token and your new password to auth/password_reset/confirm/"

    send_mail(
        # title:
        "Password Reset for {title}".format(title="food reservation system"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )        