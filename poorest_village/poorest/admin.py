from django.contrib import admin
from django.apps import apps
from .models import User,Government,School,Infrastructure,Center,Village,Medical,Holly_places,public_safety


class GovernmentAdmin(admin.ModelAdmin):
    list_display = ("__str__")

admin.site.register(User)
admin.site.register(Government)
admin.site.register(School)
admin.site.register(Village)
admin.site.register(Center)
admin.site.register(Medical)
admin.site.register(Holly_places)
admin.site.register(Infrastructure)
admin.site.register(public_safety)
