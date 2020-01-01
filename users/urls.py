from django.urls import path

from .views import *
from .viewsets import *

app_name = "users"

urlpatterns = [
    path('list', UserList),
    path('<int:pk>', UserDetail),
    path('groups/', Grouplist),
    path('groups/<int:pk>/', GroupDetail),

    path("", view=user_redirect_view, name="redirect"),
    path("update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
