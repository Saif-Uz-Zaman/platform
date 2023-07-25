# Generated by Django 4.2.2 on 2023-07-25 08:31

import django.contrib.postgres.fields
from django.db import migrations, models
import django_lifecycle.mixins
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Attachment",
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
                ("name", models.CharField(max_length=512)),
                ("path", models.URLField()),
                ("file_type", models.CharField(blank=True, max_length=5, null=True)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Bounty",
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
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("points", models.IntegerField()),
                (
                    "status",
                    models.IntegerField(
                        choices=[
                            (0, "Draft"),
                            (1, "Blocked"),
                            (2, "Available"),
                            (3, "Claimed"),
                            (4, "Done"),
                            (5, "In review"),
                        ],
                        default=2,
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Capability",
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
                ("path", models.CharField(max_length=255, unique=True)),
                ("depth", models.PositiveIntegerField()),
                ("numchild", models.PositiveIntegerField(default=0)),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(default="", max_length=1000)),
                ("video_link", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "verbose_name_plural": "capabilities",
                "db_table": "capability",
            },
        ),
        migrations.CreateModel(
            name="CapabilityAttachment",
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
            ],
            options={
                "db_table": "capability_attachment",
            },
        ),
        migrations.CreateModel(
            name="Challenge",
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
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False)),
                ("title", models.TextField()),
                ("description", models.TextField()),
                ("short_description", models.TextField(max_length=256)),
                (
                    "status",
                    models.IntegerField(
                        choices=[
                            (0, "Draft"),
                            (1, "Blocked"),
                            (2, "Available"),
                            (3, "Claimed"),
                            (4, "Done"),
                            (5, "In review"),
                        ],
                        default=0,
                    ),
                ),
                ("blocked", models.BooleanField(default=False)),
                ("featured", models.BooleanField(default=False)),
                (
                    "priority",
                    models.IntegerField(
                        choices=[(0, "High"), (1, "Medium"), (2, "Low")], default=1
                    ),
                ),
                (
                    "published_id",
                    models.IntegerField(blank=True, default=0, editable=False),
                ),
                ("auto_approve_task_claims", models.BooleanField(default=True)),
                ("video_url", models.URLField(blank=True, null=True)),
                (
                    "skill_mode",
                    models.IntegerField(
                        choices=[(0, "Single Skill"), (1, "Multiple Skills")], default=0
                    ),
                ),
                (
                    "reward_type",
                    models.IntegerField(
                        choices=[(0, "Liquid Points"), (1, "Non-liquid Points")],
                        default=1,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Challenges",
            },
        ),
        migrations.CreateModel(
            name="ChallengeDependency",
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
            ],
            options={
                "db_table": "product_management_challenge_dependencies",
            },
        ),
        migrations.CreateModel(
            name="ChallengeListing",
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
                ("title", models.TextField()),
                ("description", models.TextField()),
                ("short_description", models.TextField(max_length=256)),
                (
                    "status",
                    models.IntegerField(
                        choices=[
                            (0, "Draft"),
                            (1, "Blocked"),
                            (2, "Available"),
                            (3, "Claimed"),
                            (4, "Done"),
                            (5, "In review"),
                        ],
                        default=0,
                    ),
                ),
                (
                    "tags",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=django.contrib.postgres.fields.ArrayField(
                            base_field=models.CharField(max_length=254), size=None
                        ),
                        size=None,
                    ),
                ),
                ("blocked", models.BooleanField(default=False)),
                ("featured", models.BooleanField(default=False)),
                (
                    "priority",
                    models.IntegerField(
                        choices=[(0, "High"), (1, "Medium"), (2, "Low")], default=1
                    ),
                ),
                (
                    "published_id",
                    models.IntegerField(blank=True, default=0, editable=False),
                ),
                ("auto_approve_task_claims", models.BooleanField(default=True)),
                ("created_by", models.JSONField()),
                ("updated_by", models.JSONField()),
                ("reviewer", models.JSONField(null=True)),
                ("product_data", models.JSONField(null=True)),
                ("video_url", models.URLField(blank=True, null=True)),
                ("task_claim", models.JSONField(null=True)),
                ("assigned_to_data", models.JSONField(null=True)),
                ("has_active_depends", models.BooleanField(default=False)),
                ("initiative_data", models.JSONField(null=True)),
                ("capability_data", models.JSONField(null=True)),
                ("in_review", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="ContributorAgreement",
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
                ("agreement_content", models.TextField()),
            ],
            options={
                "db_table": "contribution_management_contributor_agreement",
            },
        ),
        migrations.CreateModel(
            name="ContributorAgreementAcceptance",
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
                ("accepted_at", models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                "db_table": "contribution_management_contributor_agreement_acceptance",
            },
        ),
        migrations.CreateModel(
            name="ContributorGuide",
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
                ("title", models.CharField(max_length=60, unique=True)),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Initiative",
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
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False)),
                ("name", models.TextField()),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "status",
                    models.IntegerField(
                        choices=[
                            (1, "Active"),
                            (2, "Completed"),
                            (3, "Draft"),
                            (4, "Cancelled"),
                        ],
                        default=1,
                    ),
                ),
                ("video_url", models.URLField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False)),
                (
                    "photo",
                    models.CharField(
                        blank=True, default=None, max_length=1024, null=True
                    ),
                ),
                ("name", models.TextField()),
                ("short_description", models.TextField()),
                ("full_description", models.TextField(blank=True, null=True)),
                ("website", models.CharField(max_length=512)),
                ("detail_url", models.URLField(blank=True, null=True)),
                ("video_url", models.URLField(blank=True, null=True)),
                ("slug", models.SlugField(unique=True)),
                ("is_private", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
            bases=(django_lifecycle.mixins.LifecycleModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="ProductChallenge",
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
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ProductRole",
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
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False)),
                (
                    "role",
                    models.IntegerField(
                        choices=[
                            (0, "Follower"),
                            (1, "Admin"),
                            (2, "Manager"),
                            (3, "Contributor"),
                        ],
                        default=0,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Tag",
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
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("name", models.CharField(max_length=128)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
