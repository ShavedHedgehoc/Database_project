# Generated by Django 2.1.7 on 2019-03-12 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20190312_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app_test_time',
            name='prod_row',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.Production'),
        ),
        migrations.AlterField(
            model_name='conv_test_time',
            name='prod_row',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.Production'),
        ),
        migrations.AlterField(
            model_name='plug_adm_time',
            name='prod_row',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.Production'),
        ),
        migrations.AlterField(
            model_name='prod_adm_time',
            name='prod_row',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.Production'),
        ),
        migrations.AlterField(
            model_name='production',
            name='batch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Batch'),
        ),
        migrations.AlterField(
            model_name='production',
            name='p_apparatus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Apparatus'),
        ),
        migrations.AlterField(
            model_name='production',
            name='p_container',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Container'),
        ),
        migrations.AlterField(
            model_name='production',
            name='p_conveyor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Conveyor'),
        ),
        migrations.AlterField(
            model_name='suppose_times',
            name='prod_row',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.Production'),
        ),
    ]
