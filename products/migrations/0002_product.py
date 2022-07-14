# Generated by Django 4.0.6 on 2022-07-05 19:36

from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=127, unique=True, verbose_name='Reference')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True, verbose_name='Slug')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('is_featured', models.BooleanField(default=False, verbose_name='Is featured')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=16, verbose_name='Price')),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=16, verbose_name='Discount')),
                ('available', models.BooleanField(default=True, verbose_name='Available')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('brand', models.ForeignKey(default=products.models.ProductBrand.get_default, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='products', to='products.productbrand', verbose_name='Brand')),
                ('category', models.ForeignKey(default=products.models.ProductCategory.get_default, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='products', to='products.productcategory', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ('name',),
            },
        ),
    ]
