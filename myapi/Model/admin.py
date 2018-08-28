from django.contrib import admin
from models import Test, Apiconfig

# Register your models here.
admin.site.register([Test, Apiconfig])