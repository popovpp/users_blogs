# Generated by Django 3.1.1 on 2020-12-01 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ubserv', '0004_auto_20201201_2226'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-idPost'], 'verbose_name': 'Подписка', 'verbose_name_plural': 'Подписка'},
        ),
        migrations.RenameField(
            model_name='news',
            old_name='idSubscr',
            new_name='idPost',
        ),
    ]