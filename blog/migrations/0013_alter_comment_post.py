# Generated by Django 5.0.4 on 2024-04-14 19:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_tag_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='blog.post', verbose_name='Пост, к которому написан'),
        ),
    ]
