# Generated by Django 3.2.25 on 2024-10-22 16:02

from django.db import migrations
from ..models import FundingAgency


class Migration(migrations.Migration):

    dependencies = [
        ('hs_core', '0085_alter_baseresource_creator_and_more'),
    ]

    operations = [
        migrations.RunPython(FundingAgency.migrate_from_crossref_to_ror)
    ]
