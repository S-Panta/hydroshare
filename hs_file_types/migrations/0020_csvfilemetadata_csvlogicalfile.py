# Generated by Django 3.2.25 on 2024-07-23 20:56

import django.contrib.postgres.fields
import django.contrib.postgres.fields.hstore
from django.db import migrations, models
import django.db.models.deletion
import hs_core.hs_rdf


class Migration(migrations.Migration):

    dependencies = [
        ('hs_composite_resource', '0001_initial'),
        ('hs_file_types', '0019_auto_20220922_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSVFileMetaData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra_metadata', django.contrib.postgres.fields.hstore.HStoreField(default=dict)),
                ('keywords', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100, null=True), default=list, size=None)),
                ('is_dirty', models.BooleanField(default=False)),
                ('tableSchema', models.JSONField(default=dict)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, hs_core.hs_rdf.RDF_MetaData_Mixin),
        ),
        migrations.CreateModel(
            name='CSVLogicalFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataset_name', models.CharField(blank=True, max_length=255, null=True)),
                ('extra_data', django.contrib.postgres.fields.hstore.HStoreField(default=dict)),
                ('preview_data', models.TextField()),
                ('metadata', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='logical_file', to='hs_file_types.csvfilemetadata')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hs_composite_resource.compositeresource')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]