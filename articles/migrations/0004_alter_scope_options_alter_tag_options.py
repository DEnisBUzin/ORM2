# Generated by Django 5.1.1 on 2024-10-31 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_scope_is_delete'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'verbose_name_plural': 'Теги в статьях'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name_plural': 'Тэги'},
        ),
    ]
