# Generated by Django 5.0.7 on 2024-11-28 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_alter_user_managers_user_foto_cadastro'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='doc_pdf',
            field=models.FileField(null=True, upload_to='Documentos'),
        ),
    ]
