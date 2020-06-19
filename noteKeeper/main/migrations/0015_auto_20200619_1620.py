# Generated by Django 3.0.7 on 2020-06-19 10:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20200617_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='college_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.College', verbose_name='College'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='file_pdf',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='notes',
            name='file_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 19, 16, 20, 46, 434851), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='department_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.Department', verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='department_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.Department', verbose_name='Department'),
        ),
    ]
