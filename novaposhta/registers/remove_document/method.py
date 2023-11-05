from typing import List

from novaposhta.types import BaseMethod, ApiResponse
from .types import RemoveDocumentInfo


class RemoveDocumentsMethod(BaseMethod):
    called_method = "removeDocuments"
    model_type = RemoveDocumentInfo
    model_name = "ScanSheet"

    def __init__(self, api_key: str, document_refs: List[str], ref: str = None):
        super().__init__(api_key, DocumentRefs=document_refs, Ref=ref)

    def __call__(self) -> ApiResponse[RemoveDocumentInfo]:
        """Видалити експрес-накладні з реєстру """
        return super().__call__()
