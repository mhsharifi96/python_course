from django.contrib import admin
from .models import Task
from django.utils.html import format_html
from datetime import date

from django.utils.translation import gettext_lazy as _
from django.urls import reverse

@admin.action(description='Mark selected stories as published')
def make_published(modeladmin, request, queryset):
    queryset.update(priority='csuccess')

# Register your models here.
class MyModelAdmin(admin.ModelAdmin):
    # برای ایجاد ستون کاستوم 
    # description : نام سرستون
    @admin.display(description='custom col')
    def upper_case_name(self, obj):
        return ("%s %s" % (obj.title, obj.description)).upper()
    
    @admin.display(description='edit')
    def edit_btn(self, obj):
        return format_html(
            '<span class="button">edit</span>'
        )

    # فیلتر مرتب سازی بر اساس تاریخ
    date_hierarchy = 'date_of_creation'

    # نمایش ستون های دلخواه در ادمین 
    # نکته حواستون باشه این ستون ها یا باید در مدل موجود باشن یا ستون کاستوم بی خودی اسم ننویسین که ارور میخوره
    list_display = ('title','description','upper_case_name','edit_btn')

    # لینک دار شدن ستون جهت رفتن به صفحه ادیت
    list_display_links = ('edit_btn',)

    # فیلتر کردن ، بهتر به این ستون فیلد های مثل 
    # choice field 
    # اینا رو پاس بدیم
    list_filter = ('priority',)
    # save_on_top = True

    # کاستوم کردن ادرس نمایش پست 
    def view_on_site(self, obj):
        return 'https://example.com' + '/test/'
    
    # اکشن کاستوم
    actions = [make_published]


admin.site.register(Task, MyModelAdmin)


