
from apps.post import views
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
path("",views.index)]


 