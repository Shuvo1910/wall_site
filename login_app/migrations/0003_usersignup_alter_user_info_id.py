# Generated by Django 5.2.3 on 2025-06-24 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_delete_usersignup_alter_user_info_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSignUp',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=80)),
            ],
        ),
        migrations.AlterField(
            model_name='user_info',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
