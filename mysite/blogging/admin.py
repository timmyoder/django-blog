from django.contrib import admin
from blogging.models import Post, Category


class CategroyInline(admin.TabularInline):
    model = Category.posts.through


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)


class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'text', 'author', 'published_date')
    inlines = [
        CategroyInline,
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
