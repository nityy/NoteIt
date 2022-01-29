# Generated by Django 4.0.1 on 2022-01-29 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_alter_note_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='link',
            field=models.URLField(blank=True, help_text='Enter any associated URL, if any; must begin with scheme (http,https,ftp,ftps)'),
        ),
    ]
