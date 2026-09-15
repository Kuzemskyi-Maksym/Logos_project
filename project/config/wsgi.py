import os
import sys
from pathlib import Path
from django.core.wsgi import get_wsgi_application

# Додаємо корінь проєкту (де лежать додатки main, accounts тощо) до PYTHONPATH
CURRENT_DIR = Path(__file__).resolve().parent
BASE_DIR = CURRENT_DIR.parent
sys.path.append(str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()

app = application