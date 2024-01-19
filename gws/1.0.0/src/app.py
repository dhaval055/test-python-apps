import socket
import asyncio
import time
import random
import json
import requests
import secrets
import string

from walkoff_app_sdk.app_base import AppBase

from google.oauth2 import service_account
from googleapiclient.discovery import build


class Gws(AppBase):
    __version__ = "1.0.0"
    app_name = "Google Workspace Dhaval"

    def __init__(self, redis, logger, console_logger=None):
        """
        Each app should have this __init__ to set up Redis and logging.
        :param redis:
        :param logger:
        :param console_logger:
        """
        super().__init__(redis, logger, console_logger)
        
    def reset_user_password(self, service_account_file_id, subject ,user_email,new_password):
        service_account_file = self.get_file(service_account_file_id)
        service_account_info = service_account_file['data'].decode()
        return service_account_info

        def generate_secure_password(length=12):
            characters = string.ascii_letters + string.digits + string.punctuation
            secure_password = ''.join(secrets.choice(characters) for i in range(length))
            return secure_password
                
        if new_password = "":
            logging.info("Generating new password")
            new_password = generate_secure_password()

        try:
            service_account_info = json.loads(service_account_info)
        except Exception as e:
            print(f"Error loading service account file: {e}")
            return {"success": False, "message": f"Error loading service account file: {e}"}

        SCOPES = ['https://www.googleapis.com/auth/admin.directory.user']

        creds = service_account.Credentials.from_service_account_info(service_account_info, scopes=SCOPES,subject=subject)
        service = build('admin', 'directory_v1', credentials=creds)

        try:
            result = service.users().update(userKey=user_email, body={'password': new_password}).execute()
            print(f"Password for {USER_EMAIL} reset successfully.")
            return {"success": True, "message": f"Password for {USER_EMAIL} reset successfully."}
        except Exception as e:
            print(f"Error resetting password: {e}")
            return {"success": False, "message": f"Error resetting password: {e}"}

if __name__ == "__main__":
    Gws.run()
