from django.db import models

# Create your models here.
class Senka(models.Model):
    # senkaId : Integer型で主キー
    senkaId = models.IntegerField(primary_key=True)
    # maxBoxNum : Integer型
    maxBoxNum = models.IntegerField()
    # minBoxNum : Integer型
    minBoxNum = models.IntegerField()
    # senkaNum : Integer型
    senkaNum = models.IntegerField()