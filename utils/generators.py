from faker import Faker
import random

fake = Faker()

class Generators:
    @staticmethod
    def generate_email():
        return fake.email()

    @staticmethod
    def generate_name():
        return fake.first_name()

    @staticmethod
    def generate_last_name():
        return fake.last_name()

    @staticmethod
    def generate_password():
        return fake.password(length=10)
    
    @staticmethod
    def generate_address_data():
        return {
            "address": fake.street_address(),
            "city": fake.city(),
            "postcode": fake.postcode(),
            "country": "United Kingdom", # Using fixed for simplicity in dropdowns or generic
            "region": "Aberdeen" # Example region
        }
