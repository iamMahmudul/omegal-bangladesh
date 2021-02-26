from django.shortcuts import render
from App_Dealer_Login import views
app_name = 'App_Dealer_Login'
# Create your views here.
def index(request):
    return render(request, 'base.html')
