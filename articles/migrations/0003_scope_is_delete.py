# Generated by Django 5.1.1 on 2024-10-31 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag_alter_article_options_scope_article_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='scope',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]
