# Generated by Django 4.0.4 on 2022-05-18 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carservice', '0004_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderline',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_lines', to='carservice.order', verbose_name='uzsakymas'),
        ),
        migrations.AlterField(
            model_name='orderline',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_lines', to='carservice.service', verbose_name='uzsakymo eilute'),
        ),
    ]