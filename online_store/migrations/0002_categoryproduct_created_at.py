# Generated by Django 4.2.7 on 2023-11-19 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryproduct',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='дата создания'),
        ),
    ]
