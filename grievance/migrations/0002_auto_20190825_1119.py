# Generated by Django 2.1.7 on 2019-08-25 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grievance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherUsers',
            fields=[
                ('user_id', models.CharField(max_length=25, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('campus', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='champus',
        ),
        migrations.AddField(
            model_name='applicationstatus',
            name='campus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='applicationstatus',
            name='natureOfQuery',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='grievanceform',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='campus',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grievanceform',
            name='student_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='grievance.Student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]