# Generated by Django 5.1.6 on 2025-03-16 23:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0005_student_is_finished_alter_student_group_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ball',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('comment', models.TextField(blank=True, null=True)),
                ('homework', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_user.grouphomework')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_user.student')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('pay_id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_user.group')),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_user.month')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_user.student')),
            ],
        ),
    ]
