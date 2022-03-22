# Generated by Django 4.0.3 on 2022-03-19 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('label', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.CharField(choices=[('Animal', 'Animal'), ('Bird', 'Bird'), ('Text', 'Text'), ('Plant', 'Plant'), ('Fruit', 'Fruit'), ('Flower', 'Flower'), ('Corps', 'Corps')], max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
