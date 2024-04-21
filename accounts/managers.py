from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    # def _create_user(self, username, email, password, **extra_fields):
    #     if not username:
    #         raise ValueError("The given username must be set")
    #     email = self.normalize_email(email)
    #     GlobalUserModel = apps.get_model(
    #         self.model._meta.app_label, self.model._meta.object_name
    #     )
    #     username = GlobalUserModel.normalize_username(username)
    #     user = self.model(username=username, email=email, **extra_fields)
    #     user.password = make_password(password)
    #     user.save(using=self._db)
    #     return user

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
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user


    # def with_perm(
    #     self, perm, is_active=True, include_superusers=True, backend=None, obj=None
    # ):
    #     if backend is None:
    #         backends = auth._get_backends(return_tuples=True)
    #         if len(backends) == 1:
    #             backend, _ = backends[0]
    #         else:
    #             raise ValueError(
    #                 "You have multiple authentication backends configured and "
    #                 "therefore must provide the `backend` argument."
    #             )
    #     elif not isinstance(backend, str):
    #         raise TypeError(
    #             "backend must be a dotted import path string (got %r)." % backend
    #         )
    #     else:
    #         backend = auth.load_backend(backend)
    #     if hasattr(backend, "with_perm"):
    #         return backend.with_perm(
    #             perm,
    #             is_active=is_active,
    #             include_superusers=include_superusers,
    #             obj=obj,
    #         )
    #     return self.none()