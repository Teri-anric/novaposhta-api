from typing import Literal, List

from .types import InsertScanSheet
from novaposhta.types import BaseMethod, ApiResponse


class InsertDocumentsMethod(BaseMethod):
    called_method = "insertDocuments"
    model_type = InsertScanSheet
    model_name = "ScanSheet"

    def __init__(self, api_key: str, document_refs: List[str], ref: str, date: str = None):
        super().__init__(api_key, DocumentRefs=document_refs, Ref=ref, Date=date)

    def __call__(self) -> ApiResponse[InsertScanSheet]:
        return super().__call__()
