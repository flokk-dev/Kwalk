# Generated by Django 4.1.3 on 2022-11-21 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kwalk', '0002_alter_card_options_alter_folder_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='nb_cards',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
