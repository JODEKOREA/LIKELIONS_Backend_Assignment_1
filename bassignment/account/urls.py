from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout, name='logout'),
    path('signup/', signup_view, name='signup')
]