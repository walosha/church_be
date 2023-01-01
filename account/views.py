from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets, status
from rest_framework.decorators import action
from .serializers import CustomObtainTokenPairSerializer
from .serializers import CreateUserSerializer
from rest_framework.response import Response


class CustomObtainTokenPairView(TokenObtainPairView):
    """Login with email and password"""
    serializer_class = CustomObtainTokenPairSerializer


class AuthViewSets(viewsets.ModelViewSet):

    @action(methods=['POST'],
            url_path='register',
            detail=False, serializer_class=CreateUserSerializer)
    def invite_user(self, request, pk=None):
        serializer = self.get_serializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
