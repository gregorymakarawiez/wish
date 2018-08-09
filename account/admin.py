from django.contrib import admin
from .models import Employee, Unit

# Register custom models to make them viewable in admin interface
admin.site.register(Unit)
admin.site.register(Employee)
