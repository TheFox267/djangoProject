from django.contrib import admin

# Register your models here.
from account.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'gender', 'date_of_birth', 'native_city', 'languages', 'country', 'city', 'mobile_phone', 'add_phone', 'skype', 'personal_site', 'job']


admin.site.register(Profile, ProfileAdmin)
