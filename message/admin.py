from django.contrib import admin
from .models.contact import Contact


# Register your models here.


class AdminContact(admin.ModelAdmin):
    list_display = ['user_name', 'email', 'user_messages']


admin.site.register(Contact, AdminContact)
