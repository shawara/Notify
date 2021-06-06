# Generated by Django 3.2.4 on 2021-06-06 15:43

from django.db import migrations, models
import notifications.validators


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='kwargs',
            field=models.JSONField(default=dict, validators=[notifications.validators.JSONSchemaValidator(limit_value={'additionalProperties': {'type': 'string'}, 'description': 'This object format key:value  for calculated values use `$` as prefix ex: name:$customer.full_name', 'type': 'object'})]),
        ),
    ]
