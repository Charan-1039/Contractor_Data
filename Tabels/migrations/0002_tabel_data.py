# Generated by Django 4.1.5 on 2023-01-23 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tabels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tabel_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Data_Title', models.CharField(max_length=200)),
                ('Account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tabels.headaccounr_field')),
                ('Month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tabels.month_field')),
                ('Taluk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tabels.taluk_field')),
            ],
        ),
    ]