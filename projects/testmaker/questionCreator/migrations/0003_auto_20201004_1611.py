# Generated by Django 3.1 on 2020-10-04 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logreg', '0001_initial'),
        ('questionCreator', '0002_questiongroup_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questiongroup',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_groups', to='logreg.user'),
        ),
    ]
