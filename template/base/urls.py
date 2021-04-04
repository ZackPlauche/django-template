from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),
    path('create-account/', CreateAccount.as_view(), name='create_account'),

    # Logged In
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
]
