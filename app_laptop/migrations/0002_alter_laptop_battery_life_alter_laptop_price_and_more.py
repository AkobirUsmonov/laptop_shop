# Generated by Django 4.2.6 on 2023-10-20 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_laptop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='battery_life',
            field=models.IntegerField(verbose_name='battery_life'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='price',
            field=models.IntegerField(verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='ram',
            field=models.IntegerField(verbose_name='ram'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='screen_size',
            field=models.IntegerField(verbose_name='screen_size'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='storage',
            field=models.IntegerField(verbose_name='storage'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='weight',
            field=models.IntegerField(verbose_name='weight'),
        ),
    ]
