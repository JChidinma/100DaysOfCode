from filestack import Client
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.environ['FILESTACK_API_KEY']


class FileSharer:
    def __init__(self, filepath, api_key=API_KEY):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_file_link = client.upload(filepath=self.filepath)
        return new_file_link.url
