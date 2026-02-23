from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Post.objects.select_related("user").order_by("-created_at")

    def create(self, request, *args, **kwargs):
        if Post.objects.filter(user=request.user).exists():
            return Response(
                {"error": "Solo puedes crear un post"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        post = self.get_object()

        if post.user != request.user:
            return Response(
                {"error": "No puedes editar este post"},
                status=status.HTTP_403_FORBIDDEN
            )

        return super().update(request, *args, **kwargs)

    @action(detail=False, methods=["get", "put"])
    def mine(self, request):
        post = Post.objects.filter(user=request.user).first()
        
        if not post:
            return Response(
                {"detail": "No tienes ningún post"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        if request.method == "PUT":
            serializer = self.get_serializer(
                post,
                data=request.data,
                partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        
        serializer = self.get_serializer(post)
        return Response(serializer.data)
