# Generated by Django 2.2.1 on 2019-05-18 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('category', models.TextField()),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('approved', models.BooleanField()),
            ],
        ),
    ]
