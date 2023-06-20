from django.contrib import admin
from  base.models import Doctor,Patient,User,BlogPost

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(User)
admin.site.register(BlogPost)
