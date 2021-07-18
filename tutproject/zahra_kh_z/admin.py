from django.contrib import admin

# Register your models here.
# from myproject.myapp.models import my_model
from .models import Author, Genre, Book, BookInstance, MemberComment

# admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)


# http://www.learningaboutelectronics.com/Articles/How-to-display-readonly-fields-in-admin-in-Django.php
@admin.register(MemberComment)  # use register decorator
# admin.site.register(MemberComment, MemberCommentAdmin)
class MemberCommentAdmin(admin.ModelAdmin):
    fields = ['comment', 'updated', 'timestamp', ]
    # fields = (('timestamp', 'updated'), 'comment')  # To display multiple fields on the same line
    readonly_fields = ['updated', 'timestamp', ]  # displayed as read-only

    class Meta:
        # Give your model metadata by using an inner class Meta
        model = MemberComment


"""
It’s given one or more model classes to register with the ModelAdmin. 
If you’re using a custom AdminSite, pass it using the site keyword argument:
from myproject.admin_site import custom_admin_site
@admin.register(Author, Reader, Editor, site=custom_admin_site)
"""


@admin.register(BookInstance)
# admin.site.register(BookInstance, BookInstanceAdmin)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {'fields': ('book', 'imprint', 'id')}),
        # ('Availability', {'fields': ('status', 'due_back')}),
        ('Advanced options', {
            'classes': ('collapse',),  # click to expand
            # 'classes': ('wide', 'extrapretty'), # extra horizontal space
            'fields': ('status', 'due_back'),
            'description': 'my_description: use collapse',
        }),
    )


# class BooksInstanceInline(admin.TabularInline):
class BooksInstanceInline(admin.StackedInline):
    # write the name of models for which the Inline is made
    model = BookInstance
    # fields = ['id', 'status']  # InlineModelAdmin options


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

# C:\1_venv_django\python_course-main\tutproject>..\..\my_venv_django\Scripts\activate
