# Generated by Django 4.1.1 on 2022-09-26 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("management", "0003_assettypes_alter_asset_types"),
    ]

    operations = [
        migrations.AlterField(
            model_name="asset",
            name="brand",
            field=models.CharField(max_length=30, verbose_name="Brand"),
        ),
        migrations.AlterField(
            model_name="asset",
            name="model_no",
            field=models.CharField(max_length=25, verbose_name="Model Number"),
        ),
        migrations.AlterField(
            model_name="asset",
            name="price",
            field=models.FloatField(verbose_name="Price"),
        ),
        migrations.AlterField(
            model_name="asset",
            name="types",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="management.assettypes",
                verbose_name="Type",
            ),
        ),
        migrations.AlterField(
            model_name="asset",
            name="user",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Allotted to",
            ),
        ),
        migrations.AlterField(
            model_name="assettypes",
            name="type_name",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]