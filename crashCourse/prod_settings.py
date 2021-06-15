""" Production Settings """
# default: use settings from main settings.py if not overwritten
from .settings import *

import django_heroku


DEBUG = False
SECRET_KEY = os.getenv('DJANGO_CRASH_COURSE_SECRET_KEY', SECRET_KEY)
# adjust to the URL of your Heroku app
ALLOWED_HOSTS = ['django-crash-course.herokuapp.com']

# Activate Django-Heroku.
django_heroku.settings(locals())