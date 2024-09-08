from django.urls import path
from .views import signup,activate_code

app_name='accounts'

urlpatterns = [
    path('signup',signup,name='signup'),
    path('<str:username>/activate',activate_code,name='activate_code'),
]
