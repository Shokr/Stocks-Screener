import uuid

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db.models import *
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    guid = CharField(db_column='GUID', max_length=45, default=uuid.uuid1, editable=False)
    name = CharField(_("Name of User"), db_column='UserName', blank=True, max_length=255)
    mobile = CharField(_("User Mobile"), db_column='Mobile', max_length=11, validators=[
        RegexValidator(regex=r'^\+?1?\d{11,11}$', message="Phone number must be entered [01xxxxxxxxx] Num.")])
    email = CharField(_("User E-mail"),  db_column='Email', max_length=100, unique=True, blank=True, null=True, validators=[
        RegexValidator(regex=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", message="Enter Valid E-mail.")])
    date_of_birth = DateField(_("User Birthday"), db_column='Birthday', blank=True, null=True)

    REQUIRED_FIELDS = ['email']

    class Meta:
        # managed = False
        db_table = 'users'

        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return '{} - [{}]'.format(self.username, self.email)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
