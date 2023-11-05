from .registers import RegisterApi
from .documents import DocumentApi


class NovaposhtaAPI(RegisterApi, DocumentApi):
    def __init__(self, api_key: str):
        self.api_key = api_key
