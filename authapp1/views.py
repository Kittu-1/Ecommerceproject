from django.contrib.auth import get_user_model
from rest_framework import permissions, generics
from rest_framework import response, decorators, permissions, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
# from rest_framework_simplejwt.token_blacklist.models import  BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, UpdateUserSerializer, ChangePasswordSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# class LogoutAllView(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def post(self, request):
#         tokens = OutstandingToken.objects.filter(user=request.user.id)
#         for token in tokens:
#             t= BlacklistedToken.objects.get_or_create(token=token)
#
#         return Response(status=status.HTTP_205_RESET_CONTENT)


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer