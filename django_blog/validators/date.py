from django.core.validators import RegexValidator

year_validator = RegexValidator(
    regex=r'^\d{4}$',
    message='O ano deve conter exatamente 4 dígitos numéricos.',
    code='invalid_year',
)
