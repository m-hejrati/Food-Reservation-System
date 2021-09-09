from django.contrib.auth.models import User
from .models import Menu, Order
from rest_framework import viewsets, permissions
from web.serializers import MenuSerializer, OrderSerializer, UserSerializer

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAdminUser
from .serializers import MyTokenObtainPairSerializer

from json import JSONEncoder

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST



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
    # queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAdminUser]
    
    def get_queryset(self):

        date_from = self.request.GET.get('date_from', None)
        date_to = self.request.GET.get('date_to', None)

        # TODO: debug reading query body

        if date_from is not None and date_to is not None:
            queryset = Menu.objects.filter(date__range=[date_from, date_to])

        else:
            queryset = Menu.objects.all()
            # queryset = Menu.objects.filter(date__range=["2021-07-01", "2021-07-28"])

        return queryset


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


@csrf_exempt
@require_POST
def remove(request):

    entered_menu_id = request.POST['menu_id']
    entered_user_id = request.POST['user_id']

    entered_user = User.objects.get(id=entered_user_id)
    entered_menu = Menu.objects.get(id=entered_menu_id)

    real_user = request.user
    # TODO: debug AnonymousUser  

    if request.user.is_authenticated:
  
        if (real_user == IsAdminUser) or (real_user.id == entered_user_id):
            
            entered_order = Order.objects.get(user=entered_user, menu=entered_menu)
            entered_order.delete()
    
            return JsonResponse({ 
                'Removed': 'True',
                }, encoder=JSONEncoder)

        else:
            
            return JsonResponse({
                'Removed': 'False',
                'Message': 'You are not allowed to delete reserve of another user ...',
                }, encoder=JSONEncoder)

    else:
        return JsonResponse({
            'Removed': 'False',
            'Message': 'You are not authenticated ...',
            }, encoder=JSONEncoder)


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
