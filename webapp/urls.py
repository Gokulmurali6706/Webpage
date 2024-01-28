from django.urls import path
from webapp import views

urlpatterns=[
    path('webpage/',views.webpage, name="webpage")
]