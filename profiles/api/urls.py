from django.urls import path
from .views import (
    student_list_view,
    subject_edit_view)

'''
CLIENT
Base ENDPOINT /api/profiles/
'''

urlpatterns = [
    path('',student_list_view),
    path('edit/subject/<int:pk>', subject_edit_view)
]
