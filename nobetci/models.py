from django.db import models
from django.utils.translation import ugettext_lazy as _


class Gun(models.Model):
    adi = models.CharField(_('Adı'), max_length=100)

    class Meta:
        verbose_name = _('Gün')
        verbose_name_plural = _('Günler')
        ordering = ('id',)

    def __str__(self):
        return self.adi


class Saat(models.Model):
    adi = models.CharField(_('Adı'), max_length=100)

    class Meta:
        verbose_name = _('Saat')
        verbose_name_plural = _('Saatler')
        ordering = ('id',)

    def __str__(self):
        return self.adi


class Kule(models.Model):
    adi = models.CharField(_('Adı'), max_length=100)
    gunler = models.ManyToManyField(Gun, verbose_name=_('Günler'), blank=True, related_name="kuleler",
                                    related_query_name="kule", )
    saatler = models.ManyToManyField(Saat, verbose_name=_('Saatler'), blank=True, related_name="kuleler",
                                     related_query_name="kule", )

    class Meta:
        verbose_name = _('Kule')
        verbose_name_plural = _('Kuleler')
        ordering = ('adi',)

    def __str__(self):
        return self.adi


class Grup(models.Model):
    adi = models.CharField(_('Adı'), max_length=100)
    gunler = models.ManyToManyField(Gun, verbose_name=_('Günler'), blank=True, related_name="gruplar",
                                    related_query_name="grup", )
    saatler = models.ManyToManyField(Saat, verbose_name=_('Saatler'), blank=True, related_name="gruplar",
                                     related_query_name="grup", )

    class Meta:
        verbose_name = _('Grup')
        verbose_name_plural = _('Gruplar')
        ordering = ('adi',)

    def __str__(self):
        return self.adi


class Nobetci(models.Model):
    adi = models.CharField(_('Adı'), max_length=100)
    gruplar = models.ManyToManyField(Grup, verbose_name=_('Gruplar'), blank=True, related_name="nobetciler",
                                     related_query_name="nobetci", )

    class Meta:
        verbose_name = _('Nöbetçi')
        verbose_name_plural = _('Nöbetçiler')
        ordering = ('adi',)

    def __str__(self):
        return self.adi


class Nobet(models.Model):
    zaman = models.DateField()
    nobetci = models.ForeignKey(Nobetci, on_delete=models.DO_NOTHING)
    kule = models.ForeignKey(Kule, on_delete=models.DO_NOTHING)
    gun = models.ForeignKey(Gun, on_delete=models.DO_NOTHING)
    saat = models.ForeignKey(Saat, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = _('Nöbet')
        verbose_name_plural = _('Nöbetler')
        ordering = ('saat',)

    def __str__(self):
        return '%s' % self.zaman
