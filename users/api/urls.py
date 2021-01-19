from django.urls import path,include

from users.api.views import UserListAPIView
from users.api.views import UserDetailAPIView


urlpatterns = [
    path('', UserListAPIView.as_view(), name='user_list_create'),
    path('<int:pk>/', UserDetailAPIView.as_view(), name='user_rud')
]