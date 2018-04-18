from django.conf.urls import patterns
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from rest.views import PictureView

router = routers.DefaultRouter()
router.register(r'core', PictureView, base_name='inoutreports')

# router.register(r'update_status', update_status, base_name='update_status'),

urlpatterns = patterns('', url(r'^', include(router.urls)), )
