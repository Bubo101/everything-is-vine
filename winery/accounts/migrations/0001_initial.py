# Generated by Django 4.0.3 on 2022-08-22 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=110)),
                ('address', models.CharField(max_length=254)),
                ('phone', models.CharField(max_length=9)),
                ('email', models.CharField(max_length=110)),
                ('membership_level', models.SmallIntegerField()),
                ('employee', models.BooleanField()),
                ('winery_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='users', to='inventory.winery')),
            ],
        ),
    ]
