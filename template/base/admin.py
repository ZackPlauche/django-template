from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'page', 'display', 'order']
    list_filter = ('page', 'display')
    fields = (
        ('page', 'section_type'),
        ('title', 'display'),
        'order',
        ('image', 'subtitle'),
        ('button_1_link', 'button_1_text', 'button_2_link', 'button_2_text'),
    )
