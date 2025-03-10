# Generated by Django 4.1 on 2023-03-06 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tests", "0029_migration_tests_apps_get_model_20230318_0300"),
    ]

    operations = [
        migrations.RunSQL("SET LOCAL citus.multi_shard_modify_mode TO 'sequential';"),
        migrations.RunSQL("SELECT create_reference_table('auth_user');"),
        migrations.AddField(
            model_name="store",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
