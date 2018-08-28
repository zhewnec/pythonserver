from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Test(models.Model):
    name = models.CharField(max_length=20)


class Apiconfig(models.Model):
    key = models.CharField(max_length=50, blank=True, null=True)
    aes = models.CharField(db_column='AES', max_length=50, blank=True, null=True)  # Field name made lowercase.
    public_rsa_key = models.CharField(db_column='public_rsa_Key', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    private_rsa_key = models.CharField(max_length=1000, blank=True, null=True)
    name = models.CharField(max_length=10, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    testhost = models.CharField(max_length=100, blank=True, null=True)
    host = models.CharField(max_length=100, blank=True, null=True)



