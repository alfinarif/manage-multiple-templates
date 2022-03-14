# Generated by Django 3.2.8 on 2021-10-30 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='product',
        ),
        migrations.AddField(
            model_name='brand',
            name='name',
            field=models.CharField(default='test', max_length=255),
            preserve_default=False,
        ),
    ]
