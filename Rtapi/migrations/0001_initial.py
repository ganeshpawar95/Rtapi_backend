# Generated by Django 2.2 on 2020-11-19 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectname', models.CharField(default='', max_length=200)),
                ('description', models.CharField(default='', max_length=200)),
                ('targeturl', models.CharField(default='', max_length=200)),
                ('logfile', models.FileField(upload_to='')),
                ('connectiontimout', models.CharField(default='', max_length=200)),
                ('sendtimeout', models.CharField(default='', max_length=200)),
                ('receivetimeout', models.CharField(default='', max_length=200)),
            ],
        ),
    ]