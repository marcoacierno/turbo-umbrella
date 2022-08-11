from django.contrib import admin

from form.models import Config, Signup


@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
    pass


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    pass
