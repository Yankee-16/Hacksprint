# Generated by Django 3.0.7 on 2020-07-27 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0005_domain_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='thumbnail',
            field=models.ImageField(upload_to='challenge'),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='domain',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='subdomain',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
