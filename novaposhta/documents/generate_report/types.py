from novaposhta.types import BaseDataModel

class InternetDocument(BaseDataModel):
    """
    Represents information about a delivery.
    """
    Ref: str
    """
    Ідентифікатор (REF) контактної особи
    """

    DateTime: str
    """
    Дата доставки
    """

    PreferredDeliveryDate: str
    """
    Бажана дата доставки
    """

    Weight: str
    """
    Вага
    """

    SeatsAmount: str
    """
    Кількість місць відправлення, ціле число
    """

    IntDocNumber: str
    """
    Номер ІД
    """

    Cost: str
    """
    Оціночна вартість
    """

    CitySender: str
    """
    Ідентифікатор (REF) міста відправника
    """

    CityRecipient: str
    """
    Ідентифікатор (REF) міста отримувача
    """

    State: str
    """
    Штат
    """

    SenderAddress: str
    """
    Ідентифікатор (REF) адреси відправника
    """

    RecipientAddress: str
    """
    Ідентифікатор (REF) адреси отримувача
    """

    CostOnSite: str
    """
    Вартість доставки
    """

    PayerType: str
    """
    Тип платника
    """

    PaymentMethod: str
    """
    Форма розрахунку Cash/NonCash
    """

    AfterpaymentOnGoodsCost: str
    """
    Вартість зворотної доставки
    """

    PackingNumber: str
    """
    Номер пакування
    """
