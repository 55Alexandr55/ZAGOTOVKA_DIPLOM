# Generated by Django 5.1.4 on 2025-05-17 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='city',
            new_name='city_description',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='warehouse',
            new_name='warehouse_description',
        ),
        migrations.AddField(
            model_name='order',
            name='city_ref',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
