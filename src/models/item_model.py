
from datetime import datetime
from pandas import DataFrame
import pandas as pd
from src.repositories.item_repository import ItemRepository

class ItemModel:
    def __init__(self):
        self.repository = ItemRepository()


    
    def convert_and_add_items(self, data: DataFrame):
        try:
            Item = self.repository.entity
            # renombrar #falta convertir IdTiempo, por ahora es datetime
            data.columns = ["IdTienda",
                            "IdEncuesta",
                            "IdTiempo",
                            "NPS",
                            "Limpieza",
                            "InfoPrecioPromo",
                            "TiempoEspera",
                            "Amabilidad",
                            "ProductosOfrecidos",
                            "PromocionesOfrecidas",
                            "ProductoDelMes",
                            "DNI",
                            "Edad"
            ]
            columns_to_int = ["NPS",
                            "Limpieza",
                            "InfoPrecioPromo",
                            "TiempoEspera",
                            "Amabilidad",
                            "ProductosOfrecidos",
                            "PromocionesOfrecidas",
                            "Edad"
            ]

            # relleno con NA los vacios y luego con ceros
            data[columns_to_int] = data[columns_to_int].replace('', pd.NA)
            data[columns_to_int] = data[columns_to_int].astype(int, errors='ignore').fillna(-1)

            data['ProductoDelMes'] = data['ProductoDelMes'].fillna('')
            data['IdEncuesta'] = data['IdEncuesta'].fillna('')
            data['DNI'] = data['DNI'].fillna('')

            #convertir fecha a datetime y luego a string
            data['IdTiempo'] = pd.to_datetime(data['IdTiempo'], format='%d-%m-%Y %H:%M:%S').dt.strftime("%y%m%d")

            # Limpiar valores de 'DNI' considerando solo int con longitud de 8
            #data['DNI'] = data['DNI'].apply(lambda x: str(x) if isinstance(x, int) and 6 <= len(str(x)) <= 14 else ('' if (isinstance(x, str) and x.isdigit() and 6 <= len(str(x)) <= 14) else 'NULL'))
            data['DNI'] = data['DNI'].apply(lambda x: x if str(x).isdigit() and 6 <= len(str(x)) <= 14 else 'NULL')
            # Limpiar valores de 'Edad'

            def convert_age(x):
                try:
                    x = int(x)
                    if 0 < x <= 100:
                        return x
                    else:
                        return -1
                except (ValueError, TypeError):
                    return -1
                
            data['Edad'] = data['Edad'].apply(lambda x: convert_age(x))

            #modelar data con entidad
            list_entities = [Item(**row) for _, row in data.iterrows()]
            self.repository.add_items(list_entities)
            
        except Exception as e:
            print(e)
    
        

