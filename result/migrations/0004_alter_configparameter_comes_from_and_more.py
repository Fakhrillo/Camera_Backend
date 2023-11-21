# Generated by Django 4.2.3 on 2023-07-14 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0003_configparameter_comes_from'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configparameter',
            name='comes_from',
            field=models.CharField(choices=[('up', 'up'), ('left', 'left'), ('right', 'right')], max_length=10),
        ),
        migrations.AlterField(
            model_name='configparameter',
            name='line1_A_point_x',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='configparameter',
            name='line1_A_point_y',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='configparameter',
            name='line1_B_point_x',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='configparameter',
            name='line1_B_point_y',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='configparameter',
            name='line2_A_point_x',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='configparameter',
            name='line2_A_point_y',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='configparameter',
            name='line2_B_point_x',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='configparameter',
            name='line2_B_point_y',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='configparameter',
            name='square_x_bottom_right',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='configparameter',
            name='square_x_top_left',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='configparameter',
            name='square_y_bottom_right',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='configparameter',
            name='square_y_top_left',
            field=models.IntegerField(),
        ),
    ]
