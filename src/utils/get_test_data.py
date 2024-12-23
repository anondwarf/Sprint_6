import json
import os

from src.config import FilePath


class GetTestData:
    """Получение тестовых данных"""

    @staticmethod
    def get_accordion_text():
        file_name: str = "accordion_text.json"
        file_path = FilePath()
        with open(
            os.path.join(file_path.DATA_DIR, file_name),
            "r",
            encoding="utf-8",
        ) as file:
            data = json.load(file)
        return data["accordion_text"]
