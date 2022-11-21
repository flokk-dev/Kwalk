# Generated by Django 4.1.3 on 2022-11-20 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudo', models.CharField(default='pseudo_by_default', max_length=20)),
                ('name', models.CharField(default='name_by_default', max_length=50)),
                ('surname', models.CharField(default='surname_by_default', max_length=50)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kwalk.player')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name_by_default', max_length=20)),
                ('desc', models.CharField(default='desc_by_default', max_length=20)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kwalk.folder')),
            ],
        ),
    ]
