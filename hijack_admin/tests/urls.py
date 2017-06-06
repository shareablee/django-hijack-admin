"""URLs to run the tests."""
from compat import include, url

from django.contrib import admin

from hijack_admin.admin import HijackRelatedAdminMixin
from hijack_admin.tests.test_app.models import RelatedModel


@admin.register(RelatedModel)
class RelatedModelAdmin(HijackRelatedAdminMixin, admin.ModelAdmin):
    list_display = ('user', 'hijack_field')


admin.autodiscover()

urlpatterns = [
    url(r'^hijack/', include('hijack.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', include('hijack.tests.test_app.urls'))
]
