# Generated by Django 3.2.15 on 2022-11-07 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20221103_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=70)),
                ('phone', models.CharField(max_length=70)),
                ('desc', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='toy',
        ),
    ]
