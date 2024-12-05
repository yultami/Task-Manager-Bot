import os
from typing import Optional

from dotenv import load_dotenv


class Settings:
    def __init__(self):
        load_dotenv()
        self.TOKEN: Optional[str] = os.getenv('TOKEN')