from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('core.urls', namespace='core')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^menu/', include('menu.urls', namespace='menu')),
    url(r'^admin/', admin.site.urls),
]
