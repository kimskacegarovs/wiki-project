# Generated by Django 4.0.1 on 2022-01-31 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(default=2),
            preserve_default=False,
        ),
    ]
