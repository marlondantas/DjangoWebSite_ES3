# Generated by Django 2.2.7 on 2019-11-14 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='voto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('voto', models.CharField(choices=[('DC', 'DOCE'), ('SL', 'SALGADO')], max_length=2)),
            ],
        ),
    ]