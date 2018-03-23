from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TestAppConfig(AppConfig):
    name = 'tests.testapp'
    label = 'testapp'
    verbose_name = _('Test App')
