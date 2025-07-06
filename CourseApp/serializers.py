from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ValidationError
from .models import *

class AppUserSerializer(ModelSerializer):
    class Meta:
        model = AppUser
        fields = ["username","password","role"]

    def create(self, validated_data):
        return AppUser.objects.create_user(**validated_data)
    
class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ["id","title"]
    def validate_title(self,value):
        if len(value)<3:
            raise ValidationError('lenght of the title should be more than 3 letters')
        return value

class EnrollementSerializer(ModelSerializer):
    class Meta:
        model = Enrollment
        fields = "__all__"