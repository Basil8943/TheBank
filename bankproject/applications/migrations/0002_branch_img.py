# Generated by Django 3.2.5 on 2022-08-22 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='img',
            field=models.ImageField(default='timezone.now', upload_to='pics'),
            preserve_default=False,
        ),
    ]
