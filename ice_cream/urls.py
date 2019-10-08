from django.urls import path

from . import views

urlpatterns = [
    # path("<str:available>",)
    path("<int:title_id>/", views.flavors, name="flavors"),
    path("", views.title, name="title"),
]
