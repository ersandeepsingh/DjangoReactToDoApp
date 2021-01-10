from django.contrib import admin

from .models import Task,Bucket
# Register your models here.


admin.site.register(Bucket)
admin.site.register(Task)