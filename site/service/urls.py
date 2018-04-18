from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:

    # url(r'^core/', include('core.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('rest.urls', namespace="rest_api")),
    url(r'', include('core.urls', namespace='core')),

]
