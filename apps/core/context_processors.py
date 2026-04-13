
from django.conf import settings


def global_settings(request):
    return {
        "DEFAULT_CURRENCY_CODE": settings.DEFAULT_CURRENCY_CODE,
        "DEFAULT_CURRENCY_SYMBOL": settings.DEFAULT_CURRENCY_SYMBOL,
    }
