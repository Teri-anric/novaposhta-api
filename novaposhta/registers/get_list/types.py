from novaposhta.types import BaseDataModel


class ScanSheetList(BaseDataModel):
    Ref: str
    """Ідентифікатор (REF) адреси"""
    Number: str
    """Номер реєстру"""
    DateTime: str
    """Дата створення"""
    Printed: str
    """Ознака друку реєстру, якщо 1 - реєстр роздруковано, якщо 0 - реєстр не друкувався"""
