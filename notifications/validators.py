from django.core.validators import BaseValidator
import jsonschema
from rest_framework.exceptions import ValidationError


class JSONSchemaValidator(BaseValidator):
    def compare(self, input, schema):
        try:
            jsonschema.validate(input, schema)
        except jsonschema.exceptions.ValidationError as err:
            raise ValidationError(err.message)