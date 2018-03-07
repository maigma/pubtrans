from django.contrib import admin

# Register your models here.

from .models import Person, AppStopsModel, AppUsersModel

class PersonAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, PersonAdmin)
admin.site.register(AppUsersModel)
admin.site.register(AppStopsModel)
