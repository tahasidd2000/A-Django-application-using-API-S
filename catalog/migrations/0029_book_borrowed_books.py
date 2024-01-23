# Generated by Django 5.0.1 on 2024-01-23 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0028_rename_borrowed_date_borrowedbook_borrow_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='borrowed_books',
            field=models.ManyToManyField(blank=True, related_name='books', to='catalog.borrowedbook'),
        ),
    ]