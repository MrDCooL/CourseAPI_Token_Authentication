from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated
from .permissions import IsInstructor,IsStudent
# Create your views here.


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated,IsInstructor|IsStudent]

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)

class EnrollementViewSet(ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollementSerializer
    permission_classes = [IsAuthenticated,IsStudent]

class RegisterView(CreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer