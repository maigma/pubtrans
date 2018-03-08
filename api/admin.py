from django.contrib import admin

# Register your models here.

from .models import Person, AppStopsModel, AppUsersModel

class PersonAdmin(admin.ModelAdmin):
    pass

class AppStopsAdmin(admin.ModelAdmin):
	model = AppStopsModel
	list_display = ('name', 'address', 'latitude', 'longitude')

admin.site.register(Person, PersonAdmin)
admin.site.register(AppStopsModel, AppStopsAdmin)
