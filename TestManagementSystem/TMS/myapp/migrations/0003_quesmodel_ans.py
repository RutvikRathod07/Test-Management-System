# Generated by Django 4.1.7 on 2023-04-06 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_quesmodel_ans'),
    ]

    operations = [
        migrations.AddField(
            model_name='quesmodel',
            name='ans',
            field=models.CharField(max_length=1, null=True),
        ),
    ]