import re
import pandas as pd
import gspread
from src.helpers.sheet_selector import SheetSelector
from src.services.drive_service import DriveService

class FileService:
    def __init__(self, drive_service: DriveService):
        self.drive_service = drive_service
        self.sheet_selector = SheetSelector()

    def process_file(self, file_id: str) -> pd.DataFrame:
        gspread_credentials_path = "gspread_credentials.json"
        google_sheets_link = self.drive_service.get_google_sheets_link(gspread_credentials_path, file_id)
        print("FILE SERVICE. GOOGLE SHEETS LINK: " + google_sheets_link)

        try:
            if google_sheets_link:
                gc = gspread.service_account(filename='gspread_credentials.json')
                workbook = gc.open_by_url(google_sheets_link)
                sheet_name = self.sheet_selector.select_sheet(workbook)
                #sheet_name = "Abril 2024"
                sheet = workbook.worksheet(sheet_name)
                
                values = sheet.get_all_values()
                df = pd.DataFrame(values[1:], columns=values[0])

                required_columns = ['Token', 'Code', 'Date response', '¿Cuál es su DNI?', '¿Qué edad tiene?']
                
                #columnas del patron '1/9'. '2/9', hasta '8/9'
                columns_to_select = [column for column in df.columns if re.search(r'[1-8]/9:', column)]
                columns_to_select.sort(key=lambda x: int(re.search(r'(\d+)/9:', x).group(1)))

                final_columns = required_columns[:3] + columns_to_select + required_columns[3:]

                '''
                required_columns = ['Token', #StoreNo-IdTienda
                    #'Group', #NGroup-xxx
                    'Code', #Code-IdEncuesta
                    'Date response', #CreationDate-IdTiempo 
                    '1/9: En una escala del 0 al 10 donde 0 es "Definitivamente No lo Recomendaría" y 10 "Definitivamente Sí lo Recomendaría", según su última experiencia de compra en la tienda ¿Qué tan probable es que recomiende Tambo+ a sus amigos o familiares?', 
                    '2/9: En una escala del 0 al 10 donde 0 es "Nada satisfecho" y 10 "Totalmente satisfecho", ¿Qué tan satisfecho se encuentra con los siguientes aspectos? ............................................................................ LA LIMPIEZA Y ORDEN DEL LOCAL', 
                    '2/9: En una escala del 0 al 10 donde 0 es "Nada satisfecho" y 10 "Totalmente satisfecho", ¿Qué tan satisfecho se encuentra con los siguientes aspectos?  ............................................................................ LA LIMPIEZA Y ORDEN DEL LOCAL'
                    #'3/9: En una escala del 0 al 10 donde 0 es "Nada satisfecho" y 10 "Totalmente satisfecho", ¿Qué tan satisfecho se encuentra con los siguientes aspectos? ............................................................................. LA INFORMACIÓN DE PRECIOS Y PROMOCIONES (AFICHES, CARTELES, FOLLETOS)', 
                    #'4/9: En una escala del 0 al 10 donde 0 es "Nada satisfecho" y 10 "Totalmente satisfecho", ¿Qué tan satisfecho se encuentra con los siguientes aspectos? ............................................................................. EL TIEMPO DE ESPERA PARA REALIZAR EL PAGO', 
                    #'5/9: En una escala del 0 al 10 donde 0 es "Nada satisfecho" y 10 "Totalmente satisfecho", ¿Qué tan satisfecho se encuentra con los siguientes aspectos? ............................................................................. LA AMABILIDAD DEL PERSONAL QUE LO ATENDIÓ', 
                    #'6/9: En una escala del 0 al 10 donde 0 es "Nada satisfecho" y 10 "Totalmente satisfecho", ¿Qué tan satisfecho se encuentra con los siguientes aspectos? ............................................................................. LOS PRODUCTOS QUE OFRECE TAMBO+', 
                    #'7/9: En una escala del 0 al 10 donde 0 es "Nada satisfecho" y 10 "Totalmente satisfecho", ¿Qué tan satisfecho se encuentra con los siguientes aspectos? ............................................................................. LAS PROMOCIONES QUE OFRECE TAMBO+', 
                    '8/9: ¿Nuestros colaboradores le ofrecieron el producto del mes?',
                    '¿Cuál es su DNI?', #DNI
                    '¿Qué edad tiene?' #Edad
                ]
                '''
                df = df[final_columns]
                print(df.iloc[1])

        except Exception as e:
            print(f"Error al procesar Google Sheet: {e}")
            import traceback
            traceback.print_exc()

        return df
