from rest_framework.routers import DefaultRouter

from .viewsets import *

router = DefaultRouter('v1')
router.register('user', UserList)
# router.register('users/<int:pk>/', UserDetail)

urlpatterns = router.urls