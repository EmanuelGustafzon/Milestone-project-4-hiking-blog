# Generated by Django 3.2.14 on 2022-09-09 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='MountainDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('height_over_sea', models.IntegerField(blank=True)),
                ('hours_of_walking', models.IntegerField(blank=True)),
                ('difficulty_level', models.CharField(choices=[('HARD', 'hard'), ('MEDIUM', 'medium'), ('EASY', 'easy')], max_length=20, null=True)),
            ],
        ),
    ]
