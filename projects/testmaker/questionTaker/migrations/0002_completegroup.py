# Generated by Django 3.1 on 2020-10-10 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionCreator', '0006_auto_20201005_2102'),
        ('logreg', '0001_initial'),
        ('questionTaker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompleteGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complete_groups', to='questionCreator.questiongroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complete_groups', to='logreg.user')),
            ],
        ),
    ]