# Generated by Django 4.0.5 on 2022-07-04 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnitOfMeasure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.AlterField(
            model_name='stock',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='product.product'),
        ),
        migrations.AddField(
            model_name='stock',
            name='unity_of_measure',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='warehouse.unitofmeasure'),
            preserve_default=False,
        ),
    ]
