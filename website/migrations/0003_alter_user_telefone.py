# Generated by Django 5.0.4 on 2024-09-13 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_user_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telefone',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
