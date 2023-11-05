from novaposhta.types import BaseDataModel

class RemoveDocumentInfo(BaseDataModel):
    """
    Represents information about a document.
    """
    Ref: str
    """
    Ідентифікатор (REF) документу
    """

    Number: str
    """
    Номер реєстру
    """

    Error: str
    """
    Помилка, згідно якої неможливо видалити документ з реєстру
    """
