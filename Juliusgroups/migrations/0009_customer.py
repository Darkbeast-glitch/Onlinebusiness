# Generated by Django 2.0.7 on 2021-09-30 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Juliusgroups', '0008_register_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='CUstomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]