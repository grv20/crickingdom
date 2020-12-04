from django.urls import path
from .views import registration

'''
CLIENT
Base ENDPOINT /register
'''

urlpatterns = [
    path('', registration, name='register')
]