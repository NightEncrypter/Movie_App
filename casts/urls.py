from django.urls import path

from . import views

urlpatterns=[
    
    path("<str:cast_id>",views.index,name="cast")
]