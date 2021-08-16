# Generated by Django 3.2.6 on 2021-08-16 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20210816_1420'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='issuedbook',
            options={'ordering': ['issued_date', 'expiry_date'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(default='0000000000000', help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='issuedbook',
            name='expiry_date',
            field=models.DateField(blank=True, null=True, verbose_name='due date'),
        ),
        migrations.AlterField(
            model_name='issuedbook',
            name='issued_date',
            field=models.DateField(blank=True, null=True, verbose_name='issued date'),
        ),
    ]