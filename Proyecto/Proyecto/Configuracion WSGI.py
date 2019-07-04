
import os
import sys

path = '/home/fraediaz7/Django_en_PythonAnywhere.com/Proyecto'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'Proyecto.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
