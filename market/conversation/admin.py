from django.contrib import admin

from .models import Conversation, ConversationMessage

# Register your models here.


class ConversationMessageInline(admin.TabularInline):
    model = ConversationMessage
    fields = ('created_by', 'content')


class ConversationAdmin(admin.ModelAdmin):
    inlines = [ConversationMessageInline]


admin.site.register(ConversationMessage)
admin.site.register(Conversation, ConversationAdmin)
