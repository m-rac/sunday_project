from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.TicketView.as_view(), name="list"),
    path('create/', views.CreateTicketView.as_view(), name="create")
]