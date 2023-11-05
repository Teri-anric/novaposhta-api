from .types import ScanSheet
from novaposhta.types import BaseMethod, ApiResponse


class GetScanSheetMethod(BaseMethod):
    called_method = "getScanSheet"
    model_name = "ScanSheet"
    model_type = ScanSheet

    def __init__(self, api_key: str, ref: str, counterparty_ref: str) -> ApiResponse[ScanSheet]:
        super().__init__(api_key, Ref=ref, CounterpartyRef=counterparty_ref)
