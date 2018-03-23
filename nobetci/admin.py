from django.contrib import admin

from .models import Gun, Saat, Kule, Nobetci, Nobet, Grup


class GunAdmin(admin.ModelAdmin):
    list_display = ('adi',)


class SaatAdmin(admin.ModelAdmin):
    list_display = ('adi',)


class KuleAdmin(admin.ModelAdmin):
    list_display = ('adi', 'get_gunler', 'get_saatler')

    def get_gunler(self, instance):
        return ','.join([i.adi for i in instance.gunler.all()])

    def get_saatler(self, instance):
        return ','.join([i.adi for i in instance.saatler.all()])


class GrupAdmin(admin.ModelAdmin):
    list_display = ('adi', 'get_gunler', 'get_saatler')

    def get_gunler(self, instance):
        return ','.join([i.adi for i in instance.gunler.all()])

    def get_saatler(self, instance):
        return ','.join([i.adi for i in instance.saatler.all()])


class NobetciAdmin(admin.ModelAdmin):
    list_display = ('adi', 'get_gruplar')

    def get_gruplar(self, instance):
        return ','.join([i.adi for i in instance.gruplar.all()])


class NobetAdmin(admin.ModelAdmin):
    list_display = ('zaman', 'nobetci', 'kule', 'gun', 'saat')


admin.site.register(Gun, GunAdmin)
admin.site.register(Saat, SaatAdmin)
admin.site.register(Kule, KuleAdmin)
admin.site.register(Grup, GrupAdmin)
admin.site.register(Nobetci, NobetciAdmin)
admin.site.register(Nobet, NobetAdmin)
