# Generated by Django 3.2.6 on 2021-08-16 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20210816_1450'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='issuedbook',
            options={'ordering': ['issued_date', 'expiry_date'], 'permissions': (('can_mark_returned', 'Set book as returned'),), 'verbose_name_plural': 'Catalog'},
        ),
    ]