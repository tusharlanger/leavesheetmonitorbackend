# Generated by Django 2.2.3 on 2019-07-25 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Holidays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('day', models.CharField(max_length=9)),
                ('holiday', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Holidays',
            },
        ),
    ]
