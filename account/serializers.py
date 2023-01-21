from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from .managers import CustomUserManager
from rest_framework import serializers
from .models import CustomUser, ChurchGroup


class BasicUserSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = [
            'id', 'firstname', 'lastname', 'email', 'category']


class CustomObtainTokenPairSerializer(TokenObtainPairSerializer):
    serializer_class = CustomUserManager

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        firstname = serializers.CharField(required=True, write_only=True)
        lastname = serializers.CharField(required=True, write_only=True)
        model = CustomUser
        fields = ['email', 'password', 'firstname', 'lastname']
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        user = get_user_model().objects.create_user(**self.validated_data)
        return user


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(
        style={"input_type": "password"}, required=True)
    new_password = serializers.CharField(
        style={"input_type": "password"}, required=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError(
                {'current_password': 'Does not match'})
        return value


class ChurchGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChurchGroup
        fields = '__all__'


class UserChurchGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChurchGroup
        fields = ("id", 'name')


class ListUserSerializer(serializers.ModelSerializer):
    group_list = UserChurchGroupSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        order = ('-created_at')
        fields = ("id", 'email', "firstname",
                  "lastname", "category", "group_list")

    def to_representation(self, instance):
        print(instance)
        return super().to_representation(instance)
