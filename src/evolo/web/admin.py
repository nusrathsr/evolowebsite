from django.contrib import admin

from web.models import Contact, Customer, Plan, Service, Team


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id"]


admin.site.register(Customer, CustomerAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description"]


admin.site.register(Service, ServiceAdmin)


class TeamAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "designation", "facebook_url", "twitter_url"]


admin.site.register(Team, TeamAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ["id", "full_name", "email", "phone", "interested_in"]


admin.site.register(Contact, ContactAdmin)


class PlanAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "price", "short_description"]


admin.site.register(Plan, PlanAdmin)
