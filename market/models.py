from django.db.models import *
from django.db.models import QuerySet
from django.urls import reverse
from django.utils import timezone


################################ --- Soft Deletion --- ##########################################

# SoftDeletionQuerySet Model

class SoftDeletionQuerySet(QuerySet):
    @property
    def delete(self):
        return super(SoftDeletionQuerySet, self).update(time_deleted=timezone.now(), deleted=True)

    def hard_delete(self):
        return super(SoftDeletionQuerySet, self).delete()

    def alive(self):
        return self.filter(time_deteted=None)

    def dead(self):
        return self.exclude(time_deteted=None)


# SoftDeletionManager Model
class SoftDeletionManager(Manager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super(SoftDeletionManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        if self.alive_only:
            return SoftDeletionQuerySet(self.model).filter(time_deleted=None)
        return SoftDeletionQuerySet(self.model)

    def hard_delete(self):
        return self.get_queryset().hard_delete()


## SoftDeletion Model
class SoftDeletionModel(Model):
    time_deleted = DateTimeField(db_column='TimeDeleted', blank=True, null=True)
    deleted = BooleanField(db_column='Deleted', blank=True, null=True, default=False)

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    class Meta:
        abstract = True

    def delete(self):
        self.time_deleted = timezone.now()
        self.deleted = True
        self.save()

    def hard_delete(self):
        super(SoftDeletionModel, self).delete()


######################################################################################################
class Stock(SoftDeletionModel):

    symbol = CharField(db_column='Symbol', max_length=10, db_index=True)
    name = CharField(db_column='Name', max_length=100, db_index=True)
    sector = CharField(db_column='Sector', max_length=45, blank=True, null=True)

    info = TextField(db_column='Info', blank=True, null=True, verbose_name="Extra Info")

    creator = ForeignKey(to='users.User', related_name='stock_creator', on_delete=SET_NULL, db_column='Creator', blank=True, null=True)

    time_created = DateTimeField(db_column='TimeCreated', auto_created=True, default=timezone.now, blank=True, null=True)

    time_modified = DateTimeField(db_column='TimeModified', auto_now=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock'

        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'

        ordering = ['name']

    def save(self, *args, **kwargs):
        super(Stock, self).save(*args, **kwargs)

    def __str__(self):
        return '[{}] -  {}'.format(self.symbol, self.name)

    def get_absolute_url(self):
        return reverse("accounts:detail", kwargs={"pk": self.pk})
