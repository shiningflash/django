# Generated by Django 3.1.7 on 2021-03-28 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_id', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True, max_length=10000, null=True)),
            ],
            options={
                'db_table': 'departments',
                'ordering': ['department_id', 'name'],
            },
        ),
        migrations.CreateModel(
            name='UserBaseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=1000)),
                ('registered_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'users',
                'ordering': ['registered_at'],
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('userbasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='office.userbasemodel')),
                ('customer_id', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'db_table': 'customers',
            },
            bases=('office.userbasemodel',),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('userbasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='office.userbasemodel')),
                ('employee_id', models.CharField(max_length=100, unique=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office.department')),
            ],
            options={
                'db_table': 'employees',
            },
            bases=('office.userbasemodel',),
        ),
    ]