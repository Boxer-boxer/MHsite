# Generated by Django 2.1.4 on 2019-04-05 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0016_auto_20190402_2158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderonline',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='orderonline',
            name='user',
        ),
        migrations.AddField(
            model_name='orderbyctt',
            name='ordered_through',
            field=models.CharField(choices=[('online', 'Online'), ('ctt', 'CTT')], default='ctt', max_length=6),
        ),
        migrations.DeleteModel(
            name='OrderOnline',
        ),
    ]
