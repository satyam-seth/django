from django.contrib import admin
from myapp.models import Author, Book
from myapp.forms import AuthorForm

# Register your models here.

# Example - 1 (ModelAdmin Objects)
# class AuthorAdmin(admin.ModelAdmin):
#     pass


# admin.site.register(Author, AuthorAdmin)


# Example - 2 (ModelAdmin Objects)
# admin.site.register(Author)


# Example - 3 (The register decorator)
# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     pass


# Example - 4 (ModelAdmin.date_hierarchy)
# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     date_hierarchy = 'birth_date'

# Example - 5.1 (ModelAdmin.empty_value_display)
# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('name', 'title', 'birth_date')
#     empty_value_display = '-empty-'

# Example - 5.2 (ModelAdmin.empty_value_display)
# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('name', 'title', 'view_birth_date')

#     @admin.display(empty_value='???')
#     def view_birth_date(self, obj):
#         return obj.birth_date

# Example - 5 (ModelAdmin.exclude)
# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     exclude = ('birth_date',)

# Example - 6 (ModelAdmin.fields)
# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     #     fields = ('name', 'title')
#     fields = (('name', 'title'), 'birth_date')

# Example - 7 (ModelAdmin.fieldsets)
# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     # fieldsets = (
#     #     (None, {
#     #         'fields': ('name',)
#     #     }),
#     #     ('Advanced options', {
#     #         'classes': ('collapse',),
#     #         'fields': ('title', 'birth_date'),
#     #     }),
#     # )

#     # fieldsets = (
#     #     (None, {
#     #         'fields': ('name',)
#     #     }),
#     #     ('Advanced options', {
#     #         'classes': ('collapse',),
#     #         'fields': (('title', 'birth_date'),),
#     #     }),
#     # )

#     # fieldsets = (
#     #     ('Require Fields', {
#     #         'fields': (('name','title'),)
#     #     }),
#     #     ('Advanced options', {
#     #         'classes': ('collapse',),
#     #         'fields': ('birth_date',),
#     #     }),
#     # )

#     fieldsets = (
#         ('Require Fields', {
#             'fields': (('name', 'title'),)
#         }),
#         ('Advanced options', {
#             'classes': ('wide', 'extrapretty'),
#             'fields': ('birth_date',),
#             'description': 'this is description'
#         }),
#     )

# Example - 8 (ModelAdmin.filter_horizontal)
# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     filter_horizontal = ('author',)

# Example - 8 (ModelAdmin.filter_vertical)
# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     filter_vertical = ('author',)

# Example - 9 (ModelAdmin.form)
# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     exclude = ['birth_date']
#     form = AuthorForm

# Example - 10.1 (ModelAdmin.list_display)
# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('name', 'title', 'birth_date')

# Example - 10.1 (ModelAdmin.list_display)
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'birth_date')
