from src.helpers.data_uploader import DataUploader
from src.config.database_config import DatabaseConfig

from src.entities.item_entity import Item

class ItemRepository:
    def __init__(self):
        self.session = DatabaseConfig().create_session()
        self.data_uploader = DataUploader()
        self.entity = Item

    def add_items(self, list_entities: list):
        self.data_uploader.upload_data(list_entities, self.session)

    def delete_current_month_items(self):
        self.data_uploader.delete_data(self.session)