from django.urls import path
from myapp import views

urlpatterns=[

    path('adminpage/',views.adminpage, name="adminpage"),
]