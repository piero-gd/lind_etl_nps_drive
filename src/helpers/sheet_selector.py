from datetime import datetime
from gspread import Spreadsheet

class SheetSelector:
    def select_sheet(self, workbook: Spreadsheet):
        try:
            current_date = self.get_current_date()

            current_str = self.format_month(current_date.month) + str(current_date.year)
            print(current_str) #'enero2024'

            original_sheet_names = [sheet.title for sheet in workbook.worksheets()]
            sheet_names = [sheet.title.lower().replace(" ", "") for sheet in workbook.worksheets()]
            print(original_sheet_names) #['Octubre', 'Noviembre', 'Diciembre', 'Enero 2024']
            print(sheet_names) #['octubre', 'noviembre', 'diciembre', 'enero2024']

            matching_indexes = []
            for index, sheet in enumerate(sheet_names):
                if current_str in sheet:
                    matching_indexes.append(index)
            print(matching_indexes) #[3]
            
            if not matching_indexes:
                raise ValueError("No se encontró una hoja correspondiente al mes actual ("+current_str+").")

            selected_index = matching_indexes[0]
            selected_original_sheet: str = original_sheet_names[selected_index]

            return selected_original_sheet

        except Exception as e:
            print(f"Error al seleccionar la hoja: {e}")

    def format_month(self, month):
        month_mapping = {
            1: "enero", 2: "febrero", 3: "marzo", 4: "abril", 5: "mayo", 6: "junio",
            7: "julio", 8: "agosto", 9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"
        }
        return month_mapping.get(month, "")
    
    def get_current_date(self):
        current_date = datetime.now()
        
        #fecha modificable
        #current_date = current_date.replace(year=2024, month=4, day=1)
        print("FECHA UTILIZADA: "+str(current_date))
        return current_date