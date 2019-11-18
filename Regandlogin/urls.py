from django.urls import path
from . import views
app_name='Regandlogin'
urlpatterns=[path('',views.Home,name='home'),
             path('reg',views.reg,name='reg'),
             path('login',views.login,name='login'),
             ]