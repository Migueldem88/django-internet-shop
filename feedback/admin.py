from django.contrib import admin
from .models import Feedback, FeedbackItem

class FeedbackItemInline(admin.TabularInline):
    model = FeedbackItem
    raw_id_fields = ['product']

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'apellido', 'email',
    'direccion', 'codigo_postal', 'created', 'updated']
    list_filter = ['created', 'updated']
    inlines = [FeedbackItemInline]