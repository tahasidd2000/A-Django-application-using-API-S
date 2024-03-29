# Generated by Django 5.0.1 on 2024-01-30 15:42

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0027_alter_bookinstance_book_borrowedbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(help_text='13 Character ISBN number', max_length=13, unique=True, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular book across the whole library', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'Available'), ('m', 'Maintenance'), ('o', 'On loan'), ('r', 'Reserved')], default='a', help_text='Book availability', max_length=1),
        ),
    ]
