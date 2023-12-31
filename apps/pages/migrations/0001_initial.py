# Generated by Django 4.2.3 on 2023-07-18 13:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Page",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="Page id",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="(Title")),
                ("content", models.TextField(verbose_name="Content")),
                ("slug", models.SlugField(verbose_name="Slug")),
                ("timestamp", models.DateTimeField(auto_now_add=True, verbose_name="Timestamp")),
            ],
            options={
                "verbose_name": "Page",
                "verbose_name_plural": "Pages",
            },
        ),
        migrations.CreateModel(
            name="Tags",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="Tag id",
                    ),
                ),
                ("tag_name", models.CharField(max_length=50, verbose_name="Tag name")),
            ],
            options={
                "verbose_name": "Tag",
                "verbose_name_plural": "Tags",
            },
        ),
    ]
