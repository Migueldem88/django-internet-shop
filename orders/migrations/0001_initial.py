# Generated by Django 4.0.6 on 2022-07-05 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('dirección', models.CharField(max_length=250)),
                ('código_postal', models.CharField(max_length=20)),
                ('ciudad', models.CharField(max_length=100)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('pago', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-creado',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cuantidad', models.PositiveIntegerField(default=1)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='shop.product')),
            ],
        ),
    ]
