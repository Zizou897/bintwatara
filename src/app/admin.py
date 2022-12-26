from django.contrib import admin
from django.utils.safestring import mark_safe

from app.models import *
# Register your models here.


@admin.register(Web)
class WebAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "date_add", "publish")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["publish"]
    
    
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("image_view", "title", "date_add", "publish")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["publish"]
    
    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
    image_view.short_description = "Aperçu des images"


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("image_view", "title", "experience", "date_add", "publish")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["publish"]
    
    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
    image_view.short_description = "Aperçu des images"


@admin.register(ProcessOfConstruction)
class ProcessOfConstructionAdmin(admin.ModelAdmin):
    list_display = ("image_view", "title", "order", "date_add", "publish")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["publish"]
    
    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
    image_view.short_description = "Aperçu des images"


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("image_view", "name", "work", "date_add", "publish")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["publish"]
    
    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
    image_view.short_description = "Aperçu des images"


@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
    list_display = ("image_view", "name", "work", "date_add", "publish")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["publish"]
    
    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
    image_view.short_description = "Aperçu des images"


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ("name", "link", "date_add", "publish")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["publish"]
   


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("image_view", "title", "order", "date_add", "publish")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["publish"]
    
    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
    image_view.short_description = "Aperçu des images"




@admin.register(ConfigWeb)
class ConfigWebAdmin(admin.ModelAdmin):
    list_display = ("title", "titleAbout1", "date_add", "publish")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["publish"]
   


@admin.register(CompanyFeatures)
class CompanyFeaturesAdmin(admin.ModelAdmin):
    list_display = ("libele","date_add", "publish")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["publish"]
   
   
@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ("email", "date_add", "publish")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["publish"]
    


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "date_add", "publish")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["publish"]
    



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "date_add", "publish")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["publish"]
    