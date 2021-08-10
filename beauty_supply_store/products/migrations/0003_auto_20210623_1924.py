# Generated by Django 3.2.4 on 2021-06-23 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_products_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Producer',
                'verbose_name_plural': 'Producers',
            },
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'products'},
        ),
    ]