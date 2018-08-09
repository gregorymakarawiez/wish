from django.contrib import admin
from .models import Task

# Register custom models to make them viewable in admin interface
admin.site.register(Task)

