from novaposhta.registers.get_list.types import ScanSheetList
from novaposhta.types import BaseMethod, ApiResponse


class GetScanSheetListMethod(BaseMethod):
    called_method = "getScanSheetList"
    model_type = ScanSheetList
    model_name = "ScanSheetList"

    def __call__(self) -> ApiResponse[ScanSheetList]:
        """
        Завантажити список реєстрів
        """
        return super().__call__()
