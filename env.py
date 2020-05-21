import os, sys
import django
p=os.getcwd()
sys.path.append(p+'/dc2/')
sys.path = sys.path[::-1]
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dc2.settings")
django.setup()
from datacollection import models
