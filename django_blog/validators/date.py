from django.core.validators import RegexValidator

YEAR_VALIDATOR_MESSAGE = 'The year must contain exactly 4 numeric digits.'

year_validator = RegexValidator(
    regex=r'^\d{4}$',
    message=YEAR_VALIDATOR_MESSAGE,
    code='invalid_year',
)
