from django.urls import path
from .views import JavaView
urlpatterns = (
    # path('list/', person_list, name='person_list'),
    path('java/', JavaView.as_view(), name='Java'),

)
