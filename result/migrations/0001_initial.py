# Generated by Django 5.0 on 2024-02-03 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigParameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cam_MxID', models.CharField(max_length=50)),
                ('Door_orientation', models.CharField(blank=True, choices=[('Top', 'Top'), ('Bottom', 'Bottom'), ('Right', 'Right'), ('Left', 'Left')], max_length=10, null=True)),
                ('A_line_start_x', models.IntegerField(blank=True, null=True)),
                ('A_line_start_y', models.IntegerField(blank=True, null=True)),
                ('A_line_end_x', models.IntegerField(blank=True, null=True)),
                ('A_line_end_y', models.IntegerField(blank=True, null=True)),
                ('B_line_start_x', models.IntegerField(blank=True, null=True)),
                ('B_line_start_y', models.IntegerField(blank=True, null=True)),
                ('B_line_end_x', models.IntegerField(blank=True, null=True)),
                ('B_line_end_y', models.IntegerField(blank=True, null=True)),
                ('C_line_start_x', models.IntegerField(blank=True, null=True)),
                ('C_line_start_y', models.IntegerField(blank=True, null=True)),
                ('C_line_end_x', models.IntegerField(blank=True, null=True)),
                ('C_line_end_y', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StreamPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cam_MxID', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='media/')),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tracked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cam_MxID', models.CharField(max_length=50)),
                ('incoming', models.IntegerField()),
                ('outgoing', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
