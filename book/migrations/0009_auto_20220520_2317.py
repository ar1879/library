# Generated by Django 3.2.6 on 2022-05-21 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_rename_id_book_author_book_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='book_id',
        ),
        migrations.RemoveField(
            model_name='book',
            name='author_id',
        ),
    ]
