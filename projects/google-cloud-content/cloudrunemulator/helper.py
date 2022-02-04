from faker import Faker

from ctrl import get_total, save
from db import is_table, create_table

faker = Faker()


def bootstrap():
    if not (is_table('todos')):
        create_table()

    if get_total() == 0:
        for x in range(1, 6):
            save(faker.word(), faker.name())
