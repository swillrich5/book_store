# Generated by Django 4.1.1 on 2022-09-22 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0002_book_authors_book_is_bestselling_alter_book_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='authors',
            new_name='author',
        ),
    ]
