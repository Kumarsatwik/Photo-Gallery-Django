# Generated by Django 4.2.5 on 2023-09-12 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_rename_photomodel_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(),
        ),
    ]
