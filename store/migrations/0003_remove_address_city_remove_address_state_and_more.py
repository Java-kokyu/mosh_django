# Generated by Django 4.2.16 on 2024-09-25 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='city',
        ),
        migrations.RemoveField(
            model_name='address',
            name='state',
        ),
        migrations.RemoveField(
            model_name='address',
            name='street',
        ),
        migrations.AddField(
            model_name='address',
            name='address1',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='address2',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
