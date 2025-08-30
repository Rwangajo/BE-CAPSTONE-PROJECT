from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

# Serializer for User
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# ViewSet for User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
