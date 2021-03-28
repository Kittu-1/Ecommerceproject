from django.urls import path
from .views import RegisterView, ChangePasswordView, UpdateProfileView, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('account/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('account/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('account/register/', RegisterView.as_view(), name='auth_register'),
    path('account/change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('account/update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('account/logout/', LogoutView.as_view(), name='auth_logout'),
    # path('account/logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),
]