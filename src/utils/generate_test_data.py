import random
from faker import Faker


class GenerateTestData:
    """Генерация тестовых данных"""

    @staticmethod
    def create_order_data() -> dict:
        f = Faker("ru_RU")
        record = dict()
        record["first_name"] = f.first_name()
        record["last_name"] = f.last_name()
        record["address"] = f"{f.street_name()} {random.choice(range(100))}"
        record["phone_number"] = f.msisdn()
        record["date"] = f.date_between(start_date="today").strftime(
            "%d.%m.%Y"
        )
        record["comments"] = f.text(max_nb_chars=20)
        return record
