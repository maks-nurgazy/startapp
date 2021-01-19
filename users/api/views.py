from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from users.api.serializers import UserSerializer
from users.models import User


class UserListAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('pk')
        user = User.objects.get(id=kw_id)
        return user

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
