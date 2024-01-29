# middleware.py
from django.middleware.csrf import CsrfViewMiddleware

class DisableCSRFMiddleware(CsrfViewMiddleware):
    def _reject(self, request, reason):
        # Disable CSRF protection
        return None
