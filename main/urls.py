from django.urls import path
from . import views
urlpatterns = [
    path("elaborate/<str:title>",views.elab,name="index"),
    path("",views.index,name="index")
]