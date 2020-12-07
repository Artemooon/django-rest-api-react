# Generated by Django 3.1.3 on 2020-11-29 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('leads', '0002_lead_creation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='lead_onwer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
