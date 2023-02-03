from app.containers import Container
import pytest
from app.classes import ApiClient, ApiClientStub, Service
from dependency_injector import providers
import unittest.mock


@pytest.fixture(scope="function")
def container():
    return Container()


def test_before_override(container: Container):
    service = container.service_factory()
    assert isinstance(service, Service)
    assert isinstance(service.api_client, ApiClient)


def test_override(container: Container):
    """
    API Clientをスタブと差し替えるためにProvider.override()メソッドを使う
    """
    container.api_client_factory.override(providers.Factory(ApiClientStub))
    service = container.service_factory()

    assert isinstance(service.api_client, ApiClientStub)


def test_override_context_manager(container: Container):
    """
    API Clientをモックオブジェクトと差し替えるためにProvider.override()メソッドをコンテキストマネージャーとして使う
    """
    with container.api_client_factory.override(unittest.mock.Mock(ApiClient)):
        service = container.service_factory()
        assert isinstance(service.api_client, unittest.mock.Mock)


def test_reset_override(container: Container):
    """
    上書きした状態から元に戻すためにProvider.reset_override()メソッドを使う
    """
    container.api_client_factory.override(providers.Factory(ApiClientStub))
    service1 = container.service_factory()
    container.api_client_factory.reset_override()
    service2 = container.service_factory()

    assert isinstance(service1.api_client, ApiClientStub)
    assert isinstance(service2.api_client, ApiClient)
