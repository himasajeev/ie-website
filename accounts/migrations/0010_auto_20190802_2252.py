# Generated by Django 2.1 on 2019-08-02 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_roundonesubmission_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roundonesubmission',
            name='created',
        ),
        migrations.AddField(
            model_name='roundonesubmission',
            name='created_at',
            field=models.TextField(default='NONAME'),
        ),
    ]