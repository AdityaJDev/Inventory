# Generated by Django 4.1.1 on 2022-09-22 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("management", "0002_delete_users"),
    ]

    operations = [
        migrations.CreateModel(
            name="AssetTypes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "dtm_created",
                    models.DateTimeField(auto_now_add=True, verbose_name="DTM Created"),
                ),
                (
                    "dtm_updated",
                    models.DateTimeField(auto_now=True, verbose_name="DTM Updated"),
                ),
                ("type_name", models.CharField(max_length=50)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AlterField(
            model_name="asset",
            name="types",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="management.assettypes",
            ),
        ),
    ]