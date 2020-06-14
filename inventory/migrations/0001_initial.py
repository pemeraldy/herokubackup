# Generated by Django 3.0.7 on 2020-06-14 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('product_type', models.CharField(choices=[('Phone', 'Phone'), ('Laptop', 'Laptop'), ('Chargers', 'Chargers')], max_length=200, null=True)),
                ('category', models.CharField(choices=[('Incoming', 'Incoming'), ('Outgoing', 'Outgoing'), ('Available', 'Available')], max_length=200, null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('price', models.FloatField(null=True)),
                ('reoder_level', models.IntegerField(null=True)),
            ],
        ),
    ]