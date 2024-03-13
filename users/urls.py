from django.urls import path
from .views import UserView, AllUsers, UserProfileCreateAPIView

urlpatterns = [
    path('', UserProfileCreateAPIView.as_view(), name='user-create'),
    path('all/', AllUsers.as_view(), name='all-users'),
    path('<str:g_token>/', UserView.as_view(), name='user-detail'),
] 