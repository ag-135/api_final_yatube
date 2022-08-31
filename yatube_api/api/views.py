# TODO:  Напишите свой вариант
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import filters

from posts.models import Post, Group, Follow
from .serializers import PostSerializer, GroupSerializer, CommentSerializer, FollowSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsOwnerOrReadOnly
from rest_framework.pagination import LimitOffsetPagination


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly, ]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [AllowAny, ]


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly, ]

    def get_queryset(self):
        return get_object_or_404(Post, id=self.kwargs.get('post_id')).comments

    def perform_create(self, serializer):
        post = Post.objects.get(pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class FollowsViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    search_fields = ("following__username",)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
