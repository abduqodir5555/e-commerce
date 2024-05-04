from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(
            email = email,
            password=password,
            is_staff = False,
            is_superuser = False,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(
            email = email,
            password = password,
            is_staff=True,
            is_superuser = True,
            is_active = True,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user
