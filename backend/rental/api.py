from rest_framework import routers

from .views import FriendViewset, BelongingViewset, BorrowedViewSet


router = routers.DefaultRouter()
router.register(r'friends', FriendViewset, basename='friends')
router.register(r'belongings', BelongingViewset, basename='belongings')
router.register(r'borrowings', BorrowedViewSet)
