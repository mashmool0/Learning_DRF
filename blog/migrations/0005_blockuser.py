# Generated by Django 5.0.7 on 2024-08-17 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
            ],
        ),
    ]
