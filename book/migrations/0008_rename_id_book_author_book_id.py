# Generated by Django 3.2.6 on 2022-05-21 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_auto_20220520_2301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='id_book',
            new_name='book_id',
        ),
    ]
