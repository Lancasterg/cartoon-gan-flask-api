from app_resources.model_resource import ModelEndpointResource


class ShinkaiEndpoint(ModelEndpointResource):
    STYLE = "shinkai"
    ENDPOINT = "/v1/shinkai"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
