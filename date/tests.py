from django.test import TestCase
import datetime
from date.models import Date
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "entropy.settings")

import django

django.setup()

now=datetime.datetime.now().strftime("%m%d")
d = Date.objects.filter(day="1001")
d=str(d)


print(d)
# Create your tests here.
