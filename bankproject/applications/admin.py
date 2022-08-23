from django.contrib import admin

# Register your models here.
from applications.models import District,Branch,Application

admin.site.register(District)
admin.site.register(Branch)
admin.site.register(Application)