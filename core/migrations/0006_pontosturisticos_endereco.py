# Generated by Django 2.2.6 on 2019-11-03 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
        ('core', '0005_auto_20191103_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontosturisticos',
            name='endereco',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='enderecos.Endereco'),
            preserve_default=False,
        ),
    ]
