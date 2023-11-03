from rest_framework import viewsets
from rest_framework import permissions

from . import models
from .models import Friend, Belonging
from . import serializers
# from .permissions import IsOwner


class FriendViewset(viewsets.ModelViewSet):
    queryset = models.Friend.objects.all()
    serializer_class = serializers.FriendSerializer


class BelongingViewset(viewsets.ModelViewSet):
    serializer_class = serializers.BelongingSerializer

    def get_queryset(self):
        user = self.request.user
        return Belonging.objects.filter(owner=user)


class BorrowedViewSet(viewsets.ModelViewSet):
    queryset = models.Borrowed.objects.all()
    serializer_class = serializers.BorrowedSerializer
