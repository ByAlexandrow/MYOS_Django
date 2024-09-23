"""
WSGI config for Mystery_Of_Story project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

#   import os
# import sys

# activate_this = os.path.expanduser('~/Django/public_html/venv/bin/activate_this.py')
#   exec(open(activate_this).read(), {'__file__': activate_this})

#  sys.path.insert(1, os.path.expanduser('~/Django/public_html/'))

# __import__('pysqlite3')
# sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Mystery_Of_Story.settings')

# application = get_wsgi_application()

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Mystery_Of_Story.settings')

application = get_wsgi_application()
