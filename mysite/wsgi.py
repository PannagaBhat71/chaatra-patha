"""
WSGI config for mysite project on local and Vercel serverless platform.
"""

import os
import sys
from pathlib import Path

# Explicitly ensure the project root directory is at the front of sys.path
# This prevents Runtime.ImportModuleError / ModuleNotFoundError on Vercel lambdas
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

if 'VERCEL' in os.environ:
    from django.core.management import call_command
    try:
        call_command('migrate', interactive=False)
    except Exception as err:
        print(f"Auto-migration notice: {err}")

app = application
