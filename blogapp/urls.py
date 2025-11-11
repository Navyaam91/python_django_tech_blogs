from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.list, name="list"),
    path('list/', views.list, name="list_page"),
    path('create/', views.create, name="create"),
    path('edit/<pk>', views.edit, name="edit"),
    path('delete/<pk>', views.delete, name="delete")
   
]
