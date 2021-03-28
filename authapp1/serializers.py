from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password



class TokenPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(TokenPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token


class TokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = TokenPairSerializer


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    Password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    Confirm_Password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'Password', 'Confirm_Password', 'email')
        # extra_kwargs = {
        # 'FirstName': {'required': True},
        # 'MiddleName':{'required':False},
        # 'LastName': {'required': True}
        # }

    def validate(self, attrs):
        if attrs['Password'] != attrs['Confirm_Password']:
            raise serializers.ValidationError({"Password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],

        )

        user.set_password(validated_data['Password'])
        user.save()

        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    Password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    Confirm_Password = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'Password', 'Confirm_Password')

    def validate(self, attrs):
        if attrs['Password'] != attrs['Confirm_Password']:
            raise serializers.ValidationError({"Password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"Previous_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

        instance.set_password(validated_data['Password'])
        instance.save()

        return instance


class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email')
        # extra_kwargs = {
        #     'FirstName': {'required': True},
        #     'LastName': {'required': True},
        # }

    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def validate_username(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError({"username": "This username is already in use."})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

        # instance.FirstName = validated_data['FirstName']
        # instance.Last_Name = validated_data['LastName']
        instance.email = validated_data['email']
        instance.username = validated_data['username']

        instance.save()

        return instance
