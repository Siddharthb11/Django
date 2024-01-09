# Generated by Django 5.0.1 on 2024-01-09 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('release_date', models.DateField()),
                ('in_theater', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='YES', max_length=3)),
                ('rating', models.FloatField()),
                ('language', models.CharField(choices=[('english', 'ENGLISH'), ('hindi', 'HINDI'), ('marathi', 'MARATHI')], default='english', max_length=7)),
            ],
        ),
    ]
