# Generated by Django 5.0.3 on 2024-03-29 15:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_rename_created_at_comment_created'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
    ]
