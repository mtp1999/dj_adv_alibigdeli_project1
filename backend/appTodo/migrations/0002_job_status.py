# Generated by Django 4.2.1 on 2023-10-07 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTodo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('done', 'Done'), ('undone', 'Undone')], default='Undone', max_length=6),
        ),
    ]
