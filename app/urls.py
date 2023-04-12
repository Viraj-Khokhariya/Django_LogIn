from django.urls import path,include
from .import views

urlpatterns = [
    path('register/',views.FirstPage,name="register"),
    path('showpage/',views.ShowPage,name="showpage"),
    path('login/',views.LoginPage,name="login"),
    path('insert/',views.InsertData,name="insert"),
    path('loginuser/',views.LoginUser,name="loginuser"),
]