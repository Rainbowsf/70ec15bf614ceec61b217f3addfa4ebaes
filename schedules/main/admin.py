from django.contrib import admin
from .models import Function
from django.utils.html import format_html
from .tasks import get_schedule
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
import os


def refresh(modeladmin, request, queryset):
    """
        Перерисовываем все графики
    """
    for item in queryset:
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


admin.site.register(Function, FunctionAdmin)  # Добавляем функции в админку и убираем юзероф и группы
admin.site.unregister(User)
admin.site.unregister(Group)
