# Generated by Django 3.0.6 on 2020-08-07 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExamCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=70)),
                ('city', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='MyExamCenter',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('school.examcenter',),
        ),
    ]
