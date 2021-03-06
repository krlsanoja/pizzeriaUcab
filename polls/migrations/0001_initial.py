# Generated by Django 2.1.4 on 2018-12-28 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ci', models.IntegerField()),
                ('nombre', models.CharField(max_length=250)),
                ('apellido', models.CharField(max_length=250)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pago', models.DateTimeField(verbose_name='fecha del pago realizado')),
                ('monto_total', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ingrediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('precio', models.FloatField()),
                ('descripcion', models.TextField(max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='metodo_pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='orden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(verbose_name='fecha de orden')),
                ('cantidad', models.IntegerField()),
                ('total', models.FloatField()),
                ('fk_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.cliente')),
                ('fk_ingrediente', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.ingrediente')),
            ],
        ),
        migrations.CreateModel(
            name='pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=200)),
                ('precio', models.FloatField()),
                ('descripcion', models.TextField(max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='efectivo',
            fields=[
                ('metodo_pago_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='polls.metodo_pago')),
                ('moneda', models.CharField(max_length=60)),
            ],
            bases=('polls.metodo_pago',),
        ),
        migrations.CreateModel(
            name='tarjeta',
            fields=[
                ('metodo_pago_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='polls.metodo_pago')),
                ('num_tarjeta', models.CharField(max_length=60)),
                ('tipo', models.CharField(max_length=60)),
            ],
            bases=('polls.metodo_pago',),
        ),
        migrations.AddField(
            model_name='orden',
            name='fk_pizza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.pizza'),
        ),
        migrations.AddField(
            model_name='factura',
            name='fk_metodo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='polls.metodo_pago'),
        ),
        migrations.AddField(
            model_name='factura',
            name='fk_orden',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='polls.orden'),
        ),
    ]
