from django.urls import path
#from . import views
#import views
from post import views
urlpatterns = [path("",views.home,name="home")]
