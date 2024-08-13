from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from popularpeople.models import People, Category, Partner


class MarriedFilter(admin.SimpleListFilter):
    title = "Status"
    parameter_name = "status"

    def lookups(self, request, model_admin):
        return [
            ('married', 'Married'),
            ('single', "Single")
        ]

    def queryset(self, request, queryset):
        if self.value == 'married':
            return queryset.filter(partner__isnull=False)
        elif self.value == 'single':
            return queryset.filter(partner__isnull=True)

    def queryset(self, request, queryset):
        return queryset

@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'slug', 'cat', 'partner', 'tags', 'photo', 'post_photo']
    #exclude = ['tags', 'is_published']
    readonly_fields = ['slug', 'post_photo']
    filter_horizontal = ['tags']
    list_display = ('id', 'title', 'time_created', 'is_published', 'cat', 'post_photo')
    list_display_links = ('title','id')
    ordering = ['-time_created', 'title']
    list_editable = ('is_published', )
    list_per_page = 10
    actions = ['set_published', 'set_draft']
    search_fields = ['title', 'cat__name']
    list_filter = ['cat__name', 'is_published']

    @admin.display(description='Description')
    def brief_info(self, people: People):
        return f"Description {len(people.content)} symbols."

    @admin.display(description='Description')
    def post_photo(self, people: People):
        if people.photo:
            return mark_safe(f"<img src='{people.photo.url}' width=50")
        else:
            return 'no photo'

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


