from googleapiclient.discovery import build
from typing import Optional
from google.oauth2 import service_account

class DriveService:
    def get_google_sheets_link(self, creds_path, file_id: str) -> Optional[str]:
        try:
            creds = self.get_credentials(creds_path)
            service = build('drive', 'v3', credentials=creds)
            file = service.files().get(fileId=file_id).execute()
            return f"https://docs.google.com/spreadsheets/d/{file['id']}"
        except Exception as e:
            print(f"Error al obtener el enlace de Google Sheets: {e}")
            return None
    
    def get_credentials(self, creds_path):
        return service_account.Credentials.from_service_account_file(creds_path)