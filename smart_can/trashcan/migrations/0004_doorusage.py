# Generated by Django 3.2.6 on 2021-08-08 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trashcan', '0003_alter_occupancy_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoorUsage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('can', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trashcan.can')),
            ],
        ),
    ]
