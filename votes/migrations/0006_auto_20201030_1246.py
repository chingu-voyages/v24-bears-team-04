# Generated by Django 3.1.2 on 2020-10-30 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0005_user_elections'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='elections',
            field=models.ManyToManyField(blank=True, to='votes.Election'),
        ),
    ]
