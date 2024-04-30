from django.core.exceptions import ValidationError


def check_instagram_url(value):
    if not ("https://www.instagram.com/" in value or "https://instagram.com/" in value):
        raise ValidationError("URL is not valid")
