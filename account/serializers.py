from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers


BookshelfUser = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    """
    Basic Register Serializer
    """
    password = serializers.CharField(min_length=6, required=True)
    password_confirm = serializers.CharField(min_length=6, required=True)

    class Meta:
        model = BookshelfUser
        fields = (
            'username',
            'email',
            'password',
            'password_confirm',
        )

    def validate_username(self, value):
        if BookshelfUser.objects.filter(username=value).exists():
            raise serializers.ValidationError('username taken')
        return value

    def validate_email(self, value):
        if BookshelfUser.objects.filter(email=value).exists():
            raise serializers.ValidationError('email taken')
        return value

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('passwords are not same')
        return attrs

    def save(self, **kwargs):
        username = self.validated_data.get('username')
        email = self.validated_data.get('email')
        password = self.validated_data.get('password')
        user = BookshelfUser.objects.create_user(
            username, email, password
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    """
    not using
    """
    class Meta:
        model = BookshelfUser
        fields = (
            'username',
            'email'
        )


class LoginSerializer(serializers.Serializer):
    """
    not used
    """
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(
                request=self.context.get('request'),
                username=username, password=password,
            )
            if not user:
                raise serializers.ValidationError(
                    'can not login',
                    code='authorization'
                )
        else:
            raise serializers.ValidationError(
                'write username and password'
            )
        attrs['user'] = user
        return attrs
