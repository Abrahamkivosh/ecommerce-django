# Generated by Django 4.2.2 on 2023-07-09 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created_date'], 'verbose_name_plural': 'Products'},
        ),
    ]
