# Generated by Django 3.2.4 on 2021-08-15 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_remove_user_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='descripcion',
            field=models.CharField(default=None, max_length=300),
        ),
    ]