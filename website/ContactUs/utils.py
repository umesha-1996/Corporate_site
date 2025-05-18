import phonenumbers
from django.core.exceptions import ValidationError

def validate_international_phone(phone_number):
    try:
        number = phonenumbers.parse(phone_number, None)  
        if not phonenumbers.is_valid_number(number):
            raise ValidationError("Invalid phone number.")
    except phonenumbers.NumberParseException:
        raise ValidationError("Invalid phone number format.")
