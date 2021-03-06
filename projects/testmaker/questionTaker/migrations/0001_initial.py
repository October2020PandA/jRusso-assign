# Generated by Django 3.1 on 2020-10-04 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('logreg', '0001_initial'),
        ('questionCreator', '0002_questiongroup_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='questionCreator.question')),
                ('question_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='questionCreator.questiongroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='logreg.user')),
            ],
        ),
    ]
