from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from .serializers import CreateUserSerializer, PasswordChangeSerializer, CustomObtainTokenPairSerializer
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

    @action(methods=['POST'],
            url_path='change_password',
            permission_classes=[permissions.IsAuthenticated],
            detail=False, serializer_class=CreateUserSerializer)
    def change_user_password(self, request, pk=None):
        serializer = PasswordChangeSerializer(
            context={'request': request}, data=request.data)
        # Another way to write is as in Line 17
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        return Response(data='Password successfully changed', status=status.HTTP_200_OK)
