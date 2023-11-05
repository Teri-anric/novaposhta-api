
from novaposhta.types import BaseDataModel

class RegistryDeleteInfo(BaseDataModel):
    """
    Represents information about a deleted registry.
    """
    Ref: str
    """
    Ідентифікатор (REF) видаленого реєстру
    """

    Number: str
    """
    Ідентифікатор (REF), номеру видаленого реєстру
    """

    Error: str
    """
    Помилка, згідно якої реєстр не видаляється
    """
