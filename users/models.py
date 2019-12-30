import uuid

from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.core.validators import RegexValidator
from django.db.models import *
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, user_name, password=None):
        """
        Creates and saves a User with the given email, national_id and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            user_name=user_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, user_name, password):
        """
        Creates and saves a superuser with the given email, national_id and password.
        """
        user = self.create_user(
            email,
            password=password,
            user_name=user_name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    guid = CharField(db_column='GUID', max_length=45, default=uuid.uuid1, editable=False)
    user_name = CharField(_("User"), db_column='UserName', max_length=255, unique=True, db_index=True)
    first_name = CharField(db_column='FirstName', max_length=45, blank=True, null=True)
    last_name = CharField(db_column='LastName', max_length=45, blank=True, null=True)
    mobile = CharField(db_column='Mobile', max_length=11, validators=[
        RegexValidator(regex=r'^\+?1?\d{11,11}$', message="Phone number must be entered [01xxxxxxxxx] Num.")])
    email = CharField(db_column='Email', max_length=100, unique=True, validators=[
        RegexValidator(regex=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", message="Enter Valid E-mail.")])
    password = CharField(db_column='Password', max_length=100)

    GENDERS = Choices(
        (0, 'MALE', _('Male')),
        (1, 'FEMALE', _('Female')),
    )

    gender = PositiveSmallIntegerField(_('Gender'), choices=GENDERS, blank=True, null=True)

    date_of_birth = DateField(db_column='Birthday', blank=True, null=True)

    address = CharField(db_column='Address1', max_length=100, verbose_name="Work Address", blank=True, null=True)

    time_created = DateTimeField(db_column='TimeCreated', auto_created=True, default=timezone.now, blank=True,
                                 null=True)
    time_modified = DateTimeField(db_column='TimeModified', auto_now=True, blank=True, null=True)

    last_login = DateTimeField(db_column='LastLogin', blank=True, null=True)
    is_active = BooleanField(db_column='IsActive', default=True, blank=True, null=True)
    is_admin = BooleanField(db_column='IsAdmin', default=False, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['email']

    class Meta:
        # managed = False
        db_table = 'users'

        verbose_name = 'User'
        verbose_name_plural = 'Users'

        ordering = ['-time_created']

    def __str__(self):
        return '{} {} - [{}]'.format(self.first_name, self.last_name, self.user_name)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def save(self, *args, **kwargs):

        self.set_password(self.password)

        if self.pk is not None:
            self.time_modified = timezone.now()

        super(User, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("user:detail", kwargs={"user_name": self.user_name})
