from django.urls import path

from .views import *

app_name = "users"

urlpatterns = [
    path("", view=user_redirect_view, name="redirect"),
    path("update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
