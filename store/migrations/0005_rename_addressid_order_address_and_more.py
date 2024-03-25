# Generated by Django 4.0.4 on 2022-05-20 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='addressID',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='cardID',
            new_name='card',
        ),
        migrations.RemoveField(
            model_name='order',
            name='colors',
        ),
        migrations.RemoveField(
            model_name='order',
            name='description',
        ),
        migrations.RemoveField(
            model_name='order',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='sale_price',
        ),
        migrations.CreateModel(
            name='Order_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.SmallIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
            options={
                'verbose_name_plural': 'Orders',
            },
        ),
    ]
