from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .serializers import StudentListSerializer
# Create your views here.
def home_view(request):
    qs = Student.objects.all()
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.all()
    serializer = StudentListSerializer(obj, many=True)
    students = serializer.data
    context = {"students":students}
    return render(request,"home.html", context)