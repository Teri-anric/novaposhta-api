from typing import Type, Any, TypeVar, Generic, List, Dict
import requests
from pydantic import BaseModel

NOVAPOSHTA_JSON_URL = "https://api.novaposhta.ua/v2.0/json/"


class BaseDataModel(BaseModel):
    pass

class BaseMethod:
    called_method: str
    model_name: str
    model_type: Type[BaseDataModel]
    method_properties: Dict[str, Any]
    api_key: str

    def __init__(self, api_key: str, **method_properties: Any):
        self.api_key = api_key
        self.method_properties = method_properties

    def __call__(self) -> Any:
        # Параметри для запиту
        model = ApiResponse[self.model_type]

        payload = {
            "apiKey": self.api_key,
            "modelName": self.model_name,
            "calledMethod": self.called_method,
            "methodProperties": self.method_properties
        }
        response = requests.post(NOVAPOSHTA_JSON_URL, json=payload)

        if response.status_code == 200:
            return model.parse_raw(response.text)

        response.raise_for_status()


T = TypeVar('T')


class ApiResponse(Generic[T], BaseModel):
    success: bool
    data: List[T]
    errors: List[str]
    warnings: List[str]
    info: List[str]
    messageCodes: List[str]
    errorCodes: List[str]
    warningCodes: List[str]
    infoCodes: List[str]
