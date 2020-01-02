from django.urls import path

from .viewsets import *

app_name = "users"

urlpatterns = [
    path('list', UserList),
    path('<int:pk>', UserDetail),
    path('groups/', Grouplist),
    path('groups/<int:pk>/', GroupDetail),
]