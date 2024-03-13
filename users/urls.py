from django.urls import path
from .views import UserView, AllUsers, UserProfileCreateAPIView

urlpatterns = [
    path('', UserProfileCreateAPIView.as_view(), name='user-create'),
    path('all/', AllUsers.as_view(), name='all-users'),
    path('<str:pk>/', UserView.as_view(), name='user-detail'),
    # path('update-experience/<str:user_id>/', UserExperienceUpdateAPIView.as_view(), name='user-experience-update'),
] 