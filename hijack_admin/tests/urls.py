"""URLs to run the tests."""
from compat import include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hijack/', include('hijack.urls', namespace='hijack')),
    url(r'^hello/', include('hijack.tests.test_app.urls', namespace='test_app'))
]
