from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Testing API')


urlpatterns = (
    url(r'^djoser/', include('djoser.urls.authtoken')),
    url(r'^swagger/$', schema_view),
)
