"""
Custom Authentication Backend for Chaatra Patha.
Enables students to log in using either their username OR their email address,
with case-insensitive matching and whitespace tolerance.
"""

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q


class EmailOrUsernameModelBackend(ModelBackend):
    """
    Allows authentication using either username or email address.
    Handles case-insensitive comparisons and leading/trailing whitespace.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        if not username or not password:
            return None

        clean_user = str(username).strip()
        try:
            user = UserModel.objects.filter(
                Q(username__iexact=clean_user) | Q(email__iexact=clean_user)
            ).first()
            if user and user.check_password(password) and self.user_can_authenticate(user):
                return user
        except Exception:
            return None
        return None
