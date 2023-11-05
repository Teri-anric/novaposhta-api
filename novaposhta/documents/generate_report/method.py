from typing import Literal, List

from novaposhta.types import BaseMethod, ApiResponse
from .types import InternetDocument

REPORT_TYPE_LITERAL = Literal["csv", "xls"]


class GenerateReportMethod(BaseMethod):
    called_method = "generateReport"
    model_name = "InternetDocument"
    model_type = InternetDocument

    def __init__(self, api_key: str, document_refs: List[str], date_time: str,
                 report_type: REPORT_TYPE_LITERAL = "csv"):
        super().__init__(api_key=api_key, DocumentRefs=document_refs, Type=report_type, DateTime=date_time)

    def __call__(self) -> ApiResponse[InternetDocument]:
        return super().__call__()
