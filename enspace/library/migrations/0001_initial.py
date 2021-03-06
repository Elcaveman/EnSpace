# Generated by Django 3.0.5 on 2020-04-04 03:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LearningObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('illustration', models.ImageField(upload_to='')),
                ('description', models.CharField(max_length=200)),
                ('branche', models.CharField(max_length=50)),
                ('semester', models.IntegerField()),
                ('modulus', models.CharField(max_length=100)),
                ('element', models.CharField(max_length=50)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
