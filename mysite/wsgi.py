"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()

if 'VERCEL' in os.environ:
    from django.core.management import call_command
    try:
        call_command('migrate', interactive=False)
    except Exception as err:
        print(f"Auto-migration notice: {err}")

app = application
