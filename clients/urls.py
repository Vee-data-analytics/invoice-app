from .views import CreateClientView
from django.urls import path

app_name = 'clients'

urlpatterns = [
   path('createclient/', CreateClientView.as_view(), name='client_create'),
]