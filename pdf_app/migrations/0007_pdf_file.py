# Generated by Django 2.0.4 on 2018-04-28 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_app', '0006_remove_pdf_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdf',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]