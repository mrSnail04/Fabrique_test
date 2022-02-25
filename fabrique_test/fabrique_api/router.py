from rest_framework import routers
from .view import MailingViewSet, ClientViewSet

router = routers.SimpleRouter()
router.register('mailing', MailingViewSet, basename='mailing')
router.register('client', ClientViewSet, basename='client')


urlpatterns = []
urlpatterns += router.urls