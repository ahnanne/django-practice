from django.contrib import admin

from .models import ConversationMessage

# Register your models here.


class ConversationMessageInline(admin.TabularInline):
    model = ConversationMessage
    fields = ('created_by', 'content', 'created_at')


class ConversationAdmin(admin.ModelAdmin):
    inlines = [ConversationMessageInline]
