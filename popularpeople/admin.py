from django.contrib import admin, messages

from popularpeople.models import People, Category, Partner


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_created', 'is_published', 'cat', 'brief_info')
    list_display_links = ('title','id')
    ordering = ['-time_created', 'title']
    list_editable = ('is_published', )
    list_per_page = 10
    actions = ['set_published', 'set_draft']

    @admin.display(description='Description')
    def brief_info(self, people: People):
        return f"Description {len(people.content)} symbols."

    @admin.action(description="Publish chosen articles")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=People.Status.PUBLISHED)
        self.message_user(request, f"{count} articles changed ")

    @admin.action(description="Unpublish chosen articles")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=People.Status.DRAFT)
        self.message_user(request, f"{count} articles unpublished ", messages.WARNING)

#admin.site.register(People, PeopleAdmin)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name','id')


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name','id')


