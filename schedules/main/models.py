from django.db import models


class Function(models.Model):
    function = models.CharField(max_length=50, verbose_name='Функция')
    schedule = models.ImageField(upload_to='schedules', editable=False, blank=True, verbose_name='График')
    interval = models.FloatField(verbose_name='Интервал, t дней')
    step = models.FloatField(verbose_name='Шаг, t часов')
    created = models.DateTimeField(auto_now=True, verbose_name='Дата обработки')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'График'
        verbose_name_plural = 'Графики'

    def save(self, *args, **kwargs):
        """
            Переопределяем сохранение обьекта модели и вызываем celery task
        """
        super().save(*args, **kwargs)   # Сохраняем 1 раз чтобы было откуда брать айдишник

        from .tasks import get_schedule  # Импорт здесь, чтобы избежать Circular import Error
        get_schedule.delay(self.id)
        self.schedule = "schedules/saved_figure{}.png".format(self.id)

        super().save(*args, **kwargs)

