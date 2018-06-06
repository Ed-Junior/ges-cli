
from django.urls import path
from .views import person_list
from .views import person_new, person_update, person_delete
from .views import PersonList, PersonDetail, PersonCreate, PersonUpdate, PersonDelete, BulkView




urlpatterns = (
    path('list/', person_list, name='person_list'),
    path('new/', person_new, name='person_new'),
    path('update/<int:id>/', person_update, name='person_update'),
    path('delete/<int:id>/', person_delete, name='person_delete'),
    path('list2/', PersonList.as_view(), name='PersonList'),
    path('detail/<int:pk>/', PersonDetail.as_view(), name='person_detail'),
    path('create/', PersonCreate.as_view(), name='person_create'),
    path('nupdate/<int:pk>/', PersonUpdate.as_view(), name='person-update'),
    path('ndelete/<int:pk>/', PersonDelete.as_view(), name='person-delete'),
    path('bulk/', BulkView.as_view(), name='bulk'),



)
