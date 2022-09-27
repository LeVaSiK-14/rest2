# Generated by Django 4.1.1 on 2022-09-27 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
                ('time_start', models.TimeField()),
                ('time_end', models.TimeField()),
                ('address', models.CharField(max_length=127)),
            ],
            options={
                'verbose_name': 'Магазин',
                'verbose_name_plural': 'Магазины',
                'db_table': 'shop',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
                ('price', models.PositiveIntegerField(default=0)),
                ('replace_from', models.CharField(max_length=127)),
                ('replace_to', models.CharField(max_length=127)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='mainapp.shop')),
            ],
            options={
                'verbose_name': 'Билет',
                'verbose_name_plural': 'Билеты',
                'db_table': 'ticket',
            },
        ),
    ]