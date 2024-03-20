# Generated by Django 4.0.5 on 2024-03-20 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'books_subject',
            },
        ),
    ]