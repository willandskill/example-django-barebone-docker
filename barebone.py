import os
import sys

from django.conf import settings

DEBUG = True

SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost, 127.0.0.1').split(',')

settings.configure(
    DEBUG=True,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)

# This part should reside in `views.py`
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Hello World</h1>')

# This part should reside in `urls.py`
from django.conf.urls import url

urlpatterns = (
    url(r'^$', index),
)

# This part should reside in wsgi.py
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
app = get_wsgi_application()


# This part should reside in manage.py
if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
