from novaposhta.types import BaseDataModel


class ScanSheet(BaseDataModel):
    Ref: str
    """Ідентифікатор"""
    Number: str
    """Номер реєстру"""
    DateTime: str
    """Дата створення"""
    Count: str
    """Кількість документів в реєстрі"""
    CitySenderRef: str
    """Ідентифікатор (REF) міста відправника"""
    CitySender: str
    """Текстовий опис міста відправника"""
    SenderAddressRef: str
    """Ідентифікатор адреси відправника"""
    SenderAddress: str
    """Текстовий опис адреси відправника"""
    SenderRef: str
    """Ідентифікатор (REF) контрагента відправника"""
    Sender: str
    """Текстовий опис контрагента відправника"""
