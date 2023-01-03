from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from .serializers import CreateUserSerializer, PasswordChangeSerializer, CustomObtainTokenPairSerializer, ListUserSerializer
from rest_framework.response import Response
from .models import CustomUser


class CustomObtainTokenPairView(TokenObtainPairView):
    """Login with email and password"""
    serializer_class = CustomObtainTokenPairSerializer


class AuthViewSets(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    # serializer_class = ListUserSerializer

    def get_serializer_class(self):
        print('get_serializer_class', self.action)
        if self.action == 'list':
            return ListUserSerializer
        if self.action == 'create':
            return CreateUserSerializer
        return super().get_serializer_class()

    @action(methods=['POST'],
            url_path='register',
            detail=False)
    def register(self, request, pk=None):
        serializer = self.get_serializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['POST'],
            url_path='change_password',
            permission_classes=[permissions.IsAuthenticated],
            detail=False)
    def change_user_password(self, request, pk=None):
        serializer = PasswordChangeSerializer(
            context={'request': request}, data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        return Response(data='Password successfully changed', status=status.HTTP_200_OK)
