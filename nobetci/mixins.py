from django.db import models


class TimeStampMixin(models.Model):
    """
    A mixin to automatically generate created and updated Date attributes for Models
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
