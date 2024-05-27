from datetime import date
from sqlalchemy.orm import Session
from src.entities.item_entity import Item
from src.helpers.sheet_selector import SheetSelector

class DataUploader:
    def upload_data(self, list_entities, session: Session):
        try:
            self.delete_data(session)
            session.bulk_save_objects(list_entities)
            #session.add(list_entities[20662])
            session.commit()
            print("Data uploaded.")
        except Exception as e:
            print(f"Error al subir datos a la base de datos: {e}")
        finally:
            session.close()
    
    def delete_data(self, session: Session):
        try:
            current_date = SheetSelector.get_current_date(self)
            current_first_day = int(current_date.replace(day=1).strftime('%y%m%d'))
            print("Current first day: " + str(current_first_day))
            session.query(Item).filter(Item.IdTiempo >= current_first_day).delete()
            session.commit()
        except Exception as e:
            print(f"Error al eliminar datos del mes: {e}")
        finally:
            session.close()
        