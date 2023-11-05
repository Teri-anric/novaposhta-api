from typing import List

from .add_document import InsertDocumentsMethod
from .get_info import GetScanSheetMethod
from .get_list import GetScanSheetListMethod
from .delete import DeleteScanSheetMethod
from .remove_document import RemoveDocumentsMethod



class RegisterApi:
    api_key: str

    def get_info_register(self, ref: str, counterparty_ref: str):
        """
        Завантажує інформацію за вказаними ідентифікаторами реєстру та контрагента.

        Args:
            ref (str): Ідентифікатор (REF) реєстру. Довжина 36 символів.
            counterparty_ref (str): Ідентифікатор (REF) контрагента. Довжина 36 символів.
        """
        method = GetScanSheetMethod(self.api_key, ref=ref, counterparty_ref=counterparty_ref)
        return method()

    def add_documents_retister(self, document_refs: List[str], ref: str, date: str = None):
        """
        Запит для отримання повного звіту за накладними.

        Args:
          document_refs (List[str]): Список ідентифікаторів документів.
          ref (str): Ідентифікатор реєстру, якщо потрібно додати документ у вже створений реєстр.
          date (str, optional): Дата, якщо потрібно створити реєстр на певну дату. Defaults to None.
        """
        method = InsertDocumentsMethod(self.api_key, document_refs=document_refs, ref=ref, date=date)
        return method()

    def get_registers(self):
        """
        Завантажити список реєстрів
        """
        method = GetScanSheetListMethod(self.api_key)
        return method()

    def delete_register(self, register_refs: List[str]):
        """
        Видалити (розформувати) реєстр відправлень

        :param register_refs: Масив ідентифікаторів реєстрів
        """
        method = DeleteScanSheetMethod(self.api_key, register_refs=register_refs)
        return method()

    def remove_documents_register(self, document_refs: List[str], ref: str):
        """
        Видалити експрес-накладні з реєстру

        :param document_refs: Масив ідентифікаторів на документи, що необхідно видалити
        :param ref: Ідентифікатор (REF) реєстру
        """
        method = RemoveDocumentsMethod(self.api_key, document_refs=document_refs, ref=ref)
        return method()
