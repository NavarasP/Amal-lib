# Generated by Django 4.0.3 on 2022-04-18 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_takenbooks_fines_takenbooks_renewaldat_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='takenbooks',
            old_name='fines',
            new_name='fine',
        ),
        migrations.RenameField(
            model_name='takenbooks',
            old_name='renewaldat',
            new_name='renewaldate',
        ),
        migrations.RenameField(
            model_name='takenbooks',
            old_name='renewalstat',
            new_name='renewalstatus',
        ),
        migrations.RenameField(
            model_name='takenbooks',
            old_name='returnstat',
            new_name='returnstatus',
        ),
    ]