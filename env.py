import os, sys
import django
sys.path.append('/Users/rongbinzheng/Downloads/scrna_geo_gse/dc2/')
sys.path = sys.path[::-1]
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dc2.settings")
django.setup()
from datacollection import models
