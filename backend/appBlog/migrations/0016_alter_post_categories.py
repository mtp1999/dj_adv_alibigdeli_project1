# Generated by Django 3.2.22 on 2023-12-24 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBlog', '0015_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(blank=True, db_table='appBlog_post_category', to='appBlog.Category'),
        ),
    ]