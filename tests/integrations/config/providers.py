from src.masonite.providers import (
    RouteProvider,
    FrameworkProvider,
    ViewProvider,
    WhitenoiseProvider,
    ExceptionProvider,
    MailProvider,
    SessionProvider,
    QueueProvider,
    CacheProvider,
    EventProvider,
    StorageProvider,
    HelpersProvider,
    BroadcastProvider,
    AuthenticationProvider,
    AuthorizationProvider,
    HashServiceProvider,
    PresetsProvider,
    SecurityProvider,
    ORMProvider,
    RateProvider,
)


from src.masonite.scheduling.providers import ScheduleProvider
from src.masonite.notification.providers import NotificationProvider
from src.masonite.validation.providers.ValidationProvider import ValidationProvider
from src.masonite.api.providers import ApiProvider
from ..test_package import MyTestPackageProvider

from tests.integrations.providers import AppProvider

PROVIDERS = [
    FrameworkProvider,
    HelpersProvider,
    SecurityProvider,
    RateProvider,
    RouteProvider,
    ViewProvider,
    WhitenoiseProvider,
    ExceptionProvider,
    MailProvider,
    NotificationProvider,
    SessionProvider,
    CacheProvider,
    QueueProvider,
    ScheduleProvider,
    EventProvider,
    StorageProvider,
    BroadcastProvider,
    HashServiceProvider,
    AuthenticationProvider,
    AuthorizationProvider,
    ValidationProvider,
    PresetsProvider,
    MyTestPackageProvider,
    AppProvider,
    ORMProvider,
    ApiProvider,
]
