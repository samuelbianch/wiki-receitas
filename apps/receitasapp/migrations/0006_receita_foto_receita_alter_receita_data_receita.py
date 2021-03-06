# Generated by Django 4.0.2 on 2022-02-16 00:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitasapp', '0005_receita_publicada_alter_receita_data_receita'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='foto_receita',
            field=models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y'),
        ),
        migrations.AlterField(
            model_name='receita',
            name='data_receita',
            field=models.DateField(blank=True, verbose_name=datetime.datetime(2022, 2, 15, 21, 31, 21, 915364)),
        ),
    ]
