# Generated by Django 3.2.4 on 2021-06-03 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mynews', '0008_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=255),
        ),
    ]