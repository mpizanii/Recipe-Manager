# Generated by Django 5.1.6 on 2025-02-14 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0009_remove_usuario_first_name_remove_usuario_last_login_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(max_length=200),
        ),
    ]
