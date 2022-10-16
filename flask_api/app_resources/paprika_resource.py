from app_resources.model_resource import ModelEndpointResource


class PaprikaEndpoint(ModelEndpointResource):
    STYLE = "paprika"
    ENDPOINT = "/v1/paprika"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
