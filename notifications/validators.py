from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
import jsonschema


class JSONSchemaValidator(BaseValidator):
    def compare(self, input, schema):
        try:
            jsonschema.validate(input, schema)
        except jsonschema.exceptions.ValidationError:
            raise ValidationError(
                '%(value)s failed JSON schema check', params={'value': input})