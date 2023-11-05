from typing import List, Optional

from pydantic import BaseModel

from novaposhta.types import BaseDataModel


class LogItem(BaseModel):
    """Представляє об'єкт помилки."""
    Ref: str
    Error: str


class RegistryData(BaseModel):
    """Дані реєстру, включаючи помилки, попередження та успішні додавання."""
    Errors: List[LogItem]
    Success: List[LogItem]
    Warnings: List[LogItem]


class InsertScanSheet(BaseDataModel):
    """Представляє об'єкт результату додавання до реєстру."""
    Description: str
    """Назва реєстру (якщо було вказано при створенні)"""
    Ref: str
    """Ідентифікатор (REF) документу"""
    Number: str
    """Номер реєстру"""
    Date: str
    """Дата реєстру"""
    Errors: List[str]
    """Масив у якому вказані логічні помилки щодо збереження або оновлення реєстру"""
    Warnings: List[str]
    """Масив у якому вказана додаткова інформація про помилки щодо збереження або оновлення реєстру"""
    Data: Optional[RegistryData]
    """Об'єкт у якому вказана інформація про помилки щодо документів які не вдалось додати до реєстру."""
    Success: Optional[List[LogItem]]
    """Масив у якому вказані успішно додані до реєстру документи."""
