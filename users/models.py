from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db.models import CharField, DateField, PositiveSmallIntegerField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)

    mobile = CharField(db_column='Mobile', max_length=11, validators=[
        RegexValidator(regex=r'^\+?1?\d{11,11}$', message="Phone number must be entered [01xxxxxxxxx] Num.")])

    GENDERS = (
        (1, _("Male")),
        (2, _("Female")),
    )
    gender = PositiveSmallIntegerField(db_column='Gender', choices=GENDERS, blank=True, null=True)

    date_of_birth = DateField(db_column='Birthday', blank=True, null=True)

    address = CharField(db_column='Address1', max_length=100, verbose_name="Work Address", blank=True, null=True)

    class Meta:
        db_table = 'users'

        verbose_name = 'User'
        verbose_name_plural = 'Users'

        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.first_name+' '+self.last_name
        super(User, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
