# Generated by Django 3.1.6 on 2021-02-05 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leads',
            name='city',
            field=models.CharField(choices=[('Carinhanha', 'Carinhanha'), ('Malhada', 'Malhada'), ('Guanambi', 'Guanambi')], default='Carinhanha', max_length=50),
        ),
    ]
