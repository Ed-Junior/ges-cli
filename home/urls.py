from django.urls import path,include
from .views import home, my_logout, HomeViews, MyView
from django.views.generic.base import TemplateView
from django.contrib.auth import urls


urlpatterns = [
    path('', home, name='home'),
    path('logout/', my_logout, name='logout'),
    path('home2/', TemplateView.as_view(template_name='home2.html'),name='home2'),
    path('home3/', HomeViews.as_view(),name='home3'),
    path('view/', MyView.as_view(), name='myview'),
    path('', include(urls)),

     ]