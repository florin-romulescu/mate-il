from django.contrib import admin
from .models import Post, Attachment, Announce

# Register your models here.
class FileInline(admin.TabularInline):
    model = Post.attachments.through
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'external_url']
    search_fields = ['title', 'description', 'author']
    # list_filter = ['date', 'author']
    # date_hierarchy = 'date'
    inlines = [FileInline]

@admin.register(Announce)
class AnnounceAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'content']
    # list_filter = ['created_at']
    # date_hierarchy = 'created_at'

@admin.register(Attachment)
class AttachmentsAdmin(admin.ModelAdmin):
    list_display = ['attachment']
    search_fields = ['attachment']

