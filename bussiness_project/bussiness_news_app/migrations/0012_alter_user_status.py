# Generated by Django 3.2.12 on 2022-04-02 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bussiness_news_app', '0011_alter_user_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('editor', 'EDITOR'), ('pedestrian', 'PEDESTRIAN')], default='pedestrian', max_length=10),
        ),
    ]
