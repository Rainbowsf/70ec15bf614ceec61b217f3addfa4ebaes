# Generated by Django 3.2.6 on 2021-08-19 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210817_1046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='function',
            options={'ordering': ('-created',), 'verbose_name': 'Запись', 'verbose_name_plural': 'Записи'},
        ),
    ]
