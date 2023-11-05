from .types import RegistryDeleteInfo
from novaposhta.types import BaseMethod, ApiResponse
from typing import List

class DeleteScanSheetMethod(BaseMethod):
    called_method = "deleteScanSheet"
    model_type = RegistryDeleteInfo
    model_name = "ScanSheet"

    def __init__(self, api_key, register_refs: List[str]):
        super().__init__(api_key=api_key, ScanSheetRefs=register_refs)

    def __call__(self) -> ApiResponse[RegistryDeleteInfo]:
        return super().__call__()
