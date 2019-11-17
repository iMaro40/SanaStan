from django.contrib import admin
from forum.models import ForumTopic, Post, Title

class TitlesInline(admin.TabularInline):
    model = Title

class PostInline(admin.TabularInline):
    model = Post

class ForumTopicAdmin(admin.ModelAdmin):
    list_display = ['topic']
    inlines = [TitlesInline]
class PostAdmin(admin.ModelAdmin):
    list_display = ['topic','author','title','time_posted']

class TitleAdmin (admin.ModelAdmin):
    list_display = ['title','topic','id','creator']
    inlines = [PostInline]
admin.site.register(Title,TitleAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(ForumTopic,ForumTopicAdmin)
