from django.contrib import admin
from .models import posts , organisation , contactOrg , achievement , event

# Register your models here.

admin.site.register(posts)
admin.site.register(organisation)
admin.site.register(contactOrg)
admin.site.register(achievement)
admin.site.register(event)
