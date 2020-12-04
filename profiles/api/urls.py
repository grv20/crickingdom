from django.urls import path
from .views import (
    student_list_view)

'''
CLIENT
Base ENDPOINT /api/profiles/
'''

urlpatterns = [
    path('',student_list_view),
    
    
]
