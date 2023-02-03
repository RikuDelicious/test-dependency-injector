from dependency_injector import containers, providers
from .classes import ApiClient, Service


class Container(containers.DeclarativeContainer):
    api_client_factory = providers.Factory(ApiClient)
    service_factory = providers.Factory(Service, api_client=api_client_factory)
