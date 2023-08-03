from django.contrib import admin
from.models import courses
from.models import features
from.models import trainers
from.models import products



# Register your models here.
admin.site.register(features)
admin.site.register(courses)
admin.site.register(trainers)
admin.site.register(products)
