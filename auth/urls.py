from django.urls import re_path
from auth.views import MyObtainTokenPairView, RegisterView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    re_path(r'^login/?$', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    re_path(r'login/refresh/?$', TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'register/?$', RegisterView.as_view(), name='auth_register'),
]