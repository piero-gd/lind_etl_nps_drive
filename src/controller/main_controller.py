from src.models.item_model import ItemModel
from src.services.drive_service import DriveService
from src.services.file_service import FileService
from src.helpers.sheet_selector import SheetSelector

class MainController:
    def __init__(self, file_id: str):
        self.file_id = file_id
        self.drive_service = DriveService()
        self.file_service = FileService(self.drive_service)
        self.itemModel = ItemModel()

    def run(self):
        try:    
            data_df = self.file_service.process_file(self.file_id)
            self.itemModel.convert_and_add_items(data_df)
            #SheetSelector.get_current_date()

        except Exception as e:
            print(f"Error al procesar archivos: {e}")
            print(e)