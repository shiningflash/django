# Generated by Django 3.1.6 on 2021-02-15 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentid', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
            ],
        ),
    ]