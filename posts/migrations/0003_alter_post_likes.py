# Generated by Django 4.1.1 on 2022-09-23 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_post_like_count_remove_post_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.PositiveIntegerField(blank=True, db_index=True, default=0, verbose_name='likes'),
        ),
    ]
