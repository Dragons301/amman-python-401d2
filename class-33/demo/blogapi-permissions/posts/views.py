from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializer import PostSerializer
from .models import Post
from .permissions import PermissionsClass

# Create your views here.
class PostsListView(ListAPIView, CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (PermissionsClass, IsAuthenticated)

class PostDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (PermissionsClass, IsAuthenticated)
