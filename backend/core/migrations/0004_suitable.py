# Generated by Django 2.2 on 2021-10-18 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_aircraft_itinerary_travel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suitable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=500)),
                ('dist', models.FloatField()),
                ('cost', models.FloatField()),
                ('aircraft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suitable_aircraft', to='core.Aircraft')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
