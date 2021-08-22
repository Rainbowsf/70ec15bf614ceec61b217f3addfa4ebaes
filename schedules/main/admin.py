from django.contrib import admin
from .models import Function
from django.utils.html import format_html
from .tasks import get_schedule
import os


def refresh(modeladmin, request, queryset):
    """
        Пересчитываем все графики
    """
    for item in queryset:
        """
        script_path = os.path.abspath(__file__)
        path_list = script_path.split(os.sep)
        directory = path_list[0:len(path_list)-2]
        rel_path = "media/schedules/saved_figure{}.png".format(item.id)
        path = '/'.join(directory) + '/' + rel_path
        os.remove(path)"""
        get_schedule.delay(item.id)
        item.save()
    refresh.short_description = "Обновить"


class FunctionAdmin(admin.ModelAdmin):

    def schedule_img(self, obj):
        """
            Отображение графиков.пнг
        """
        return format_html('<img src="{}" width ="300px"/>'.format(obj.schedule.url))

    schedule_img.short_description = 'График'

    list_display = ['function', 'schedule_img', 'interval', 'step', 'created']
    ordering = ['-created']
    actions = [refresh]


admin.site.register(Function, FunctionAdmin)
