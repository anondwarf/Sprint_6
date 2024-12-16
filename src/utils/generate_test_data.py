from faker import Faker


class GenerateTestData:
    """Генерация тестовых данных"""

    @staticmethod
    def generate_first_name() -> str:
        return Faker("ru_RU").first_name()

    @staticmethod
    def generate_last_name() -> str:
        return Faker("ru_RU").last_name()

    @staticmethod
    def generate_address() -> str:
        return Faker("ru_RU").street_address()

    @staticmethod
    def generate_phone_number() -> str:
        return Faker("ru_RU").phone_number()

    @staticmethod
    def generate_date() -> str:
        return Faker("ru_RU").date()
