# Generated by Django 3.1.5 on 2021-01-12 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='owner',
            new_name='user',
        ),
    ]