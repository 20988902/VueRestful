from django.contrib import admin

# Register your models here.

from app01 import models

admin.site.register(models.Course)
admin.site.register(models.CourseDetail)
admin.site.register(models.Chapter)
