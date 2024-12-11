# Generated by Django 5.1.4 on 2024-12-11 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Food', 'Food'), ('Transport', 'Transport'), ('Utilities', 'Utilities'), ('Other', 'Other')], max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
