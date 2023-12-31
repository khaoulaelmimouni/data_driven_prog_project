# Generated by Django 4.2.7 on 2023-11-13 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='farmer',
            fields=[
                ('f_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('password', models.CharField(max_length=200)),
                ('street', models.CharField(default='', max_length=30)),
                ('city', models.CharField(default='', max_length=30)),
                ('district', models.CharField(default='', max_length=30)),
                ('phone', models.CharField(default=0, max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='sell_animal',
            fields=[
                ('animal_id', models.AutoField(primary_key=True, serialize=False)),
                ('animal_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=20)),
                ('animal_race', models.CharField(default='', max_length=20)),
                ('price', models.IntegerField()),
                ('photo', models.CharField(max_length=200)),
                ('f_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='famer', to='farmer.farmer')),
            ],
        ),
        migrations.DeleteModel(
            name='Character',
        ),
        migrations.DeleteModel(
            name='Equipement',
        ),
        migrations.AddField(
            model_name='buy',
            name='f_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='farmer', to='farmer.farmer'),
        ),
        migrations.AddField(
            model_name='buy',
            name='p_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sell', to='farmer.sell_animal'),
        ),
    ]
