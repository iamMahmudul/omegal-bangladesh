from django.urls import path
from . import views
app_name = 'App_Dealer_Login'


urlpatterns = [
    path('', views.index, name='index'),
]
