from django.urls import path

from . import views

app_name = "ice_cream"

urlpatterns = [
    path("<int:pk>/", views.DeleteIceCream.as_view(), name="delete"),
    path("new/", views.CreateIceCream.as_view(), name="create"),
    path("results/<int:pk>", views.ResultsView.as_view(), name="results"),
    path("vote/<int:pk>", views.vote, name="vote"),
    path("<str:selection>/", views.index, name="selection"),
    path("", views.index, name="index")
]
