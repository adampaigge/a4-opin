from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model

User = get_user_model()


class SignUpForm(auth_forms.UserCreationForm):
    """SignUpForm used by django-allouth to create new users."""

    def signup(self, request, user):
        user.signup(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
        )

    class Meta:
        model = User
        fields = ('email', 'username')