import dataclasses


class ApiClient:
    pass


class ApiClientStub(ApiClient):
    pass


@dataclasses.dataclass
class Service:
    api_client: ApiClient
