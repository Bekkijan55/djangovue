from django.shortcuts import render
from .models import Task,User,Group
from .serializers import TaskSerializer, UserSerializer,GroupSerializer

# Create your views here.

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(viewsets.ModelViewSet):
	
	queryset = Task.objects.all()
	serializer_class = TaskSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('-id')
	serializer_class = UserSerializer	

class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer	


