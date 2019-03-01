# Generated by Django 2.1.7 on 2019-03-01 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='l_admission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_time', models.TimeField()),
                ('admission_batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.boil')),
            ],
        ),
    ]
