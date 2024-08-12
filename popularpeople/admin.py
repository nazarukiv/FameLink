from django.contrib import admin

from popularpeople.models import People, Category, Partner


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_created', 'is_published', 'cat')
    list_display_links = ('title','id')
    ordering = ['-time_created', 'title']
    list_editable = ('is_published', )
    list_per_page = 10

#admin.site.register(People, PeopleAdmin)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name','id')


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name','id')


