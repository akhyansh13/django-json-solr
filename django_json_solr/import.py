import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_json_solr.settings')

import django
django.setup()

from djsapp.models import text

for filename in os.listdir('json'):
	if filename.endswith('.json'):
		t = open('json/' + filename)
		y = t.read()
		text.objects.get_or_create(text=y)