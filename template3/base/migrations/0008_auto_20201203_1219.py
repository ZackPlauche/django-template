# Generated by Django 3.1.4 on 2020-12-03 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('base', '0007_businessinformation_phone_number_display'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BusinessInformation',
            new_name='BusinessInfo',
        ),
        migrations.AlterModelOptions(
            name='businessinfo',
            options={'verbose_name': 'business information'},
        ),
    ]
