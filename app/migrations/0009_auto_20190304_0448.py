# Generated by Django 2.1.1 on 2019-03-04 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20190303_0651'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='questionHint',
            field=models.TextField(default='Sample Hint'),
        ),
        migrations.AddField(
            model_name='questions',
            name='questionSolvers',
            field=models.IntegerField(default=0),
        ),
    ]