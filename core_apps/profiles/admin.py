from django.contrib import admin

from core_apps.profiles.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['pkid', 'id', 'user', 'gender', 'phone_number', 'country', 'city']
    list_filter = ['gender', 'city', 'country']
    list_display_links = ['id', 'pkid', ]


admin.site.register(Profile, ProfileAdmin)
