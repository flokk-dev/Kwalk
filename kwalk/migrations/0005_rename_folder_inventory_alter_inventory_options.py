# Generated by Django 4.1.3 on 2022-11-25 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kwalk', '0004_card_rarity'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Folder',
            new_name='Inventory',
        ),
        migrations.AlterModelOptions(
            name='inventory',
            options={'verbose_name': 'Inventory', 'verbose_name_plural': 'Inventories'},
        ),
    ]
