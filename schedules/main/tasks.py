import os
from celery import shared_task
from .models import Function
import matplotlib.pyplot as plt
import time
from PIL import Image, ImageFont, ImageDraw
import textwrap
from numpy import *
import datetime


@shared_task
def get_schedule(function_id):
    func = Function.objects.get(pk=function_id)
    try:
        """
            Рисуем график
        """
        interval = func.interval * 24 * 60 * 60                   # Берем начальные значения в unix time
        step = func.step * 60 * 60
        finish = time.time()
        start = finish - interval
        fig = plt.figure()

        t = arange(start, finish, step)                           # Формируем точки в unix time

        t_time = []
        for item in t:
            t_time.append(datetime.datetime.fromtimestamp(item))  # Формируем дату по точкам
        y = eval(func.function.replace(' ', '')[2:])

        plt.xticks(rotation=30)

        plt.plot(t_time, y)
        fig.savefig('media/schedules/saved_figure{}.png'.format(str(function_id)), dpi=100)

    except Exception as exception:
        """
            Если не сраслось с графиком рисуем ошибку...
        """
        text = textwrap.wrap(repr(exception), 45)

        max_w, max_h = 640, 480
        im = Image.new('RGB', (max_w, max_h), (0, 0, 0, 0))
        draw = ImageDraw.Draw(im)

        dir_name = os.path.dirname(__file__)                    # тут ищем шрифт
        font_path = os.path.join(dir_name, 'fonts/arial.ttf')
        font = ImageFont.truetype(font_path, 20)

        current_h, padding = 200, 10
        for line in text:                                       # Красиво формируем текст по строчкам
            wdth, hght = draw.textsize(line, font=font)
            draw.text(((max_w - wdth) / 2, current_h), line, font=font)
            current_h += hght + padding

        im.save('media/schedules/saved_figure{}.png'.format(str(function_id)))
