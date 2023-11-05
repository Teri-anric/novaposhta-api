from typing import List

from .generate_report import GenerateReportMethod, REPORT_TYPE_LITERAL


class DocumentApi:
    api_key: str

    def generate_report_document(self, document_refs: List[str], date_time: str,
                                 report_type: REPORT_TYPE_LITERAL = "csv"):
        """ Запит для отримання повного звіту за накладними
        :arg document_refs: Список документів
        :arg report_type: Форма документу для друку: xls або csv
        :arg date_time: Дата доставки
        """
        method = GenerateReportMethod(self.api_key, document_refs=document_refs, report_type=report_type,
                                      date_time=date_time)
        return method()
