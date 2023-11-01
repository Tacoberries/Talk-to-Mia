# create_data.py
import os
from mia.models import TrainData, KnowledgeBase
from miaProject import settings  # Importe as configurações do seu projeto

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mia_project.settings')
settings.configure()

from django.core.management import execute_from_command_line

execute_from_command_line(["manage.py", "shell"])

