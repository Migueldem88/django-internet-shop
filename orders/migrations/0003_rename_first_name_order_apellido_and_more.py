# Generated by Django 4.0.6 on 2022-07-06 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_options_rename_dirección_order_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='first_name',
            new_name='apellido',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='city',
            new_name='ciudad',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='postal_code',
            new_name='codigo_postal',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='address',
            new_name='direccion',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='last_name',
            new_name='nombre',
        ),
        migrations.AddField(
            model_name='order',
            name='telefono',
            field=models.CharField(default='fdf', max_length=100),
            preserve_default=False,
        ),
    ]