# Generated by Django 2.2.3 on 2019-07-23 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0004_image_pdf_youtubevideo'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='recommended',
            field=models.BooleanField(default=False),
        ),
    ]
