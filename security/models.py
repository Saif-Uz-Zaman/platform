from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


from openunited.mixins import TimeStampMixin, UUIDMixin
from talent.models import Person
from .managers import UserManager


# This model will be used for advanced authentication methods
class User(AbstractUser, TimeStampMixin):
    remaining_budget_for_failed_logins = models.PositiveSmallIntegerField(default=3)
    password_reset_required = models.BooleanField(default=False)
    is_test_user = models.BooleanField(_("Test User"), default=False)

    objects = UserManager()

    def __str__(self):
        return f"{self.username} - {self.email}"


class SignUpRequest(TimeStampMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    device_hash = models.CharField(max_length=64, null=True, blank=True)
    country = models.CharField(max_length=64, null=True, blank=True)
    region_code = models.CharField(max_length=8, null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    verification_code = models.CharField(max_length=6)
    successful = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user} - {self.successful}"


class SignInAttempt(TimeStampMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device_hash = models.CharField(max_length=64, null=True, blank=True)
    country = models.CharField(max_length=64, null=True, blank=True)
    region_code = models.CharField(max_length=8, null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    successful = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.region_code} - {self.city} - {self.country}"


class ProductRoleAssignment(TimeStampMixin, UUIDMixin):
    CONTRIBUTOR = 0
    PRODUCT_MANAGER = 1
    PRODUCT_ADMIN = 2

    ROLES = (
        (CONTRIBUTOR, "Contributor"),
        (PRODUCT_MANAGER, "Manager"),
        (PRODUCT_ADMIN, "Admin"),
    )
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    role = models.IntegerField(choices=ROLES, default=0)

    def __str__(self):
        return f"{self.person} - {self.get_role_display()}"

    def clean(self):
        from security.services import ProductRoleAssignmentService

        ProductRoleAssignmentService.is_organisation_provided(self)


class BlacklistedUsernames(models.Model):
    username = models.CharField(max_length=30, unique=True, blank=False)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "black_listed_usernames"
