# Generated by Django 3.0.5 on 2021-03-09 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_auto_20210309_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_height',
            field=models.PositiveIntegerField(default=50),
        ),
    ]