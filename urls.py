from django.conf.urls import url, include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Testing API')


urlpatterns = (
    url(r'^auth/', include('djoser.urls.authtoken')),
    url(r'^docs/$', schema_view),
)
