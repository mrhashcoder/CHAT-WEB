from django.db import models
from datetime import datetime
# Create your models here.
class message(models.Model):
    mesg = models.CharField(max_length = 70)
    date = models.DateTimeField(default = datetime.now,blank = True)
    sender = models.CharField(max_length =32)
    reciver = models.CharField(max_length = 32)
