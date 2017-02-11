from django.http import HttpResponse
from date.models import Date
from date.models import Processing
from django.shortcuts import render
import datetime
import random
def date(request):
    now = datetime.datetime.now().strftime("%m%d")
    int(now)
    current_time=datetime.datetime.now().strftime("%y.%m.%d")
    d=Date.objects.filter(day=now)
    d=str(d)
    f=d.split("\t")
    del f[0]
    d=random.choice(f)
    U=random.choice(Processing.objects.all())
    return render(request,'date.html',locals())
# Create your views here.
