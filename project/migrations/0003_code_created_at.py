# Generated by Django 5.0.6 on 2024-05-30 18:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_remove_code_type_alter_code_table_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
