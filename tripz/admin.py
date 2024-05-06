from django.contrib import admin
from .models import Blog, Destination
from .models import Hotel

admin.site.register(Destination)
admin.site.register(Hotel)
admin.site.register(Blog)

# Register your models here.
