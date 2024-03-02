from django.contrib import admin

from .models import *

# Register your models here.


admin.site.register(Product)
admin.site.register(Lesson)
admin.site.register(Group)
admin.site.register(Student)
admin.site.register(StudentGroup)