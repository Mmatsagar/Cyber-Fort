# Generated by Django 2.1.1 on 2019-03-03 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20190303_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='questionCategory',
            field=models.CharField(choices=[('JR', 'Junior'), ('SR', 'Senior')], default='JR', max_length=2),
        ),
    ]