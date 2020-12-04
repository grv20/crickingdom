from django.shortcuts import render
from ..models import Subject, Student, Teacher
from ..serializers import StudentListSerializer, TeacherListSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response


@api_view(['GET']) 
@permission_classes([IsAuthenticated])
def student_list_view(request, *args, **kwargs):
    qs = Student.objects.all()
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.all()
    serializer = StudentListSerializer(obj, many=True)
    return Response(serializer.data, status=200)