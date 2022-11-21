# Generated by Django 4.1.3 on 2022-11-20 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kwalk', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={'verbose_name': 'Card', 'verbose_name_plural': 'Cards'},
        ),
        migrations.AlterModelOptions(
            name='folder',
            options={'verbose_name': 'Folder', 'verbose_name_plural': 'Folders'},
        ),
        migrations.AlterModelOptions(
            name='player',
            options={'verbose_name': 'Player', 'verbose_name_plural': 'Players'},
        ),
        migrations.AddField(
            model_name='folder',
            name='nb_cards',
            field=models.IntegerField(default=0),
        ),
    ]