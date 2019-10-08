from django.urls import path

from . import views

app_name = "ice_cream"

urlpatterns = [
    path("<str:selection>/", views.index, name="selection"),
    path("", views.index, name="index")
]
