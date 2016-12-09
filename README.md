# Djoser Swagger App

Djoser 0.5.1 and Django Rest Swagger 3.5.3 do not currently work together. (Note that using other authorization libraries, like Django OAuth Toolkit, work as expected).

The bug is currently demonstrated if you clone and run this repo.

If using your own repo, steps to reproduce:

(1) Add `djoser` and `django-rest-swagger` to an existing Rest Framework app
(2) Add token based auth to your default permissions:

```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
}
```

(3) Add djoser and swagger to your URLs
```
from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Testing API')


urlpatterns = (
    url(r'^djoser/', include('djoser.urls.authtoken')),
    url(r'^swagger/$', schema_view),
)
```

(4) Go to `localhost:8000/swagger/` and you will see the following error:

```
TypeError at /swagger/
getattr(): attribute name must be string

Request Method: GET
Request URL: http://localhost:8000/swagger/
Django Version: 1.10.4
Python Executable: /Users/usr/src/djoser/testproject/env/bin/python
Python Version: 3.5.2
Python Path: ['/Users/usr/src/djoser-swagger-example', '/usr/local/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python35.zip', '/usr/local/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5', '/usr/local/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/plat-darwin', '/usr/local/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/lib-dynload', '/Users/usr/src/djoser/testproject/env/lib/python3.5/site-packages']
Server time: Fri, 9 Dec 2016 07:18:46 -0600
Installed Applications:
('django.contrib.auth',
 'django.contrib.contenttypes',
 'django.contrib.staticfiles',
 'rest_framework',
 'rest_framework.authtoken',
 'rest_framework_swagger',
 'djoser',
 'testapp')
Installed Middleware:
()


Traceback:

File "/Users/usr/src/djoser/testproject/env/lib/python3.5/site-packages/django/core/handlers/exception.py" in inner
  39.             response = get_response(request)

File "/Users/usr/src/djoser/testproject/env/lib/python3.5/site-packages/django/core/handlers/base.py" in _legacy_get_response
  249.             response = self._get_response(request)

File "/Users/usr/src/djoser/testproject/env/lib/python3.5/site-packages/django/core/handlers/base.py" in _get_response
  187.                 response = self.process_exception_by_middleware(e, request)

File "/Users/usr/src/djoser/testproject/env/lib/python3.5/site-packages/django/core/handlers/base.py" in _get_response
  185.                 response = wrapped_callback(request, *callback_args, **callback_kwargs)

File "/Users/usr/src/djoser/testproject/env/lib/python3.5/site-packages/django/views/decorators/csrf.py" in wrapped_view
  58.         return view_func(*args, **kwargs)

File "/Users/usr/src/djoser/testproject/env/lib/python3.5/site-packages/django/views/generic/base.py" in view
  68.             return self.dispatch(request, *args, **kwargs)

File "/Users/usr/src/djoser/testproject/env/lib/python3.5/site-packages/rest_framework/views.py" in dispatch
  477.             response = self.handle_exception(exc)

File "/Users/usr/src/djoser/testproject/env/lib/python3.5/site-packages/rest_framework/views.py" in handle_exception
  437.             self.raise_uncaught_exception(exc)

File "/Users/usr/src/djoser/testproject/env/lib/python3.5/site-packages/rest_framework/views.py" in dispatch
  474.             response = handler(request, *args, **kwargs)

File "/Users/usr/src/djoser/testproject/env/lib/python3.5/site-packages/rest_framework/schemas.py" in get
  593.             schema = generator.get_schema(request)

File "/Users/usr/src/djoser/testproject/env/lib/python3.5/site-packages/rest_framework/schemas.py" in get_schema
  242.         links = self.get_links(request)

File "/Users/usr/src/djoser/testproject/env/lib/python3.5/site-packages/rest_framework/schemas.py" in get_links
  273.             link = self.get_link(path, method, view)

File "/Users/usr/src/djoser/testproject/env/lib/python3.5/site-packages/rest_framework/schemas.py" in get_link
  381.         description = self.get_description(path, method, view)

File "/Users/usr/src/djoser/testproject/env/lib/python3.5/site-packages/rest_framework/schemas.py" in get_description
  402.         method_docstring = getattr(view, method_name, None).__doc__

Exception Type: TypeError at /swagger/
Exception Value: getattr(): attribute name must be string
Request information:
USER: AnonymousUser
```
