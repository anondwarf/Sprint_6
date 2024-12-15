import json
import os

from defenition import DATA_DIR


class GetTestData:
    """Получение тестовых данных"""

    @staticmethod
    def get_accordion_text():
        file_name: str = "accordion_text.json"
        with open(
            os.path.join(DATA_DIR, file_name),
            "r",
            encoding="utf-8",
        ) as file:
            data = json.load(file)
        return data["accordion_text"]
