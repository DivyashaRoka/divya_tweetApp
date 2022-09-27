# Generated by Django 4.1.1 on 2022-09-23 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='like_count',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.PositiveIntegerField(blank=True, db_index=True, default=0, verbose_name='like'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(blank=True, db_index=True, max_length=140, null=True, verbose_name='body'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created DateTime'),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(db_index=True, default='anonymous', max_length=14, null=True, verbose_name='name'),
        ),
    ]