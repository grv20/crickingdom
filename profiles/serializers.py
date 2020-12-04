from rest_framework import serializers

from .models import Student, Teacher, Subject

from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairView):
    @classmethod
    def get_token(cls,user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        token['username'] = user.username
        return token

class TeacherListSerializer(serializers.ModelSerializer):
    name =  serializers.SerializerMethodField(read_only=True)
    subjects = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Teacher
        fields = [
            "id",
            "name",
            "subjects"
        ]
    def get_name(self,obj):
        return obj.user.first_name + " " + obj.user.last_name

    def get_subjects(self,obj):
        subjects = []
        for subject in obj.subjects.all():
            subjects.append(subject.name)
        return subjects
    


class StudentListSerializer(serializers.ModelSerializer):
    student_name =  serializers.SerializerMethodField(read_only=True)
    username =  serializers.SerializerMethodField(read_only=True)
    teachers = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Student
        fields = ["student_name",
        "id",
        "username",
        "teachers"
        ]

    def get_student_name(self,obj):
        return obj.user.first_name + " " + obj.user.last_name
    
    def get_username(self,obj):
        return obj.user.username

    def get_teachers(self,obj):
        qs = obj.teachers.all()
        teachers = TeacherListSerializer(qs, many=True)
        # teachers = []
        # for teacher in obj.teachers.all():
        #     teachers.append(TeacherListSerializer(source=teacher))
        return teachers.data