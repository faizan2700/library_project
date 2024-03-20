# Generated by Django 4.0.5 on 2024-03-20 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mime_type', models.CharField(max_length=32)),
                ('url', models.CharField(max_length=256)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.book')),
            ],
            options={
                'db_table': 'books_format',
            },
        ),
    ]