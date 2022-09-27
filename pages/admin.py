from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Blog)
admin.site.register(Testimonial)
admin.site.register(AddDraw)
admin.site.register(AllDraw)
admin.site.register(AddWinDraw)

@admin.register(BlogComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email','body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
