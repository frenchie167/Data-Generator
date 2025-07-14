import csv
import json
from faker import Faker

fake = Faker('ru_RU')

users = []
for _ in range(10000):
    user = {
        "id": fake.uuid4(),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.unique.ascii_email(),
        "registration_date": fake.date_between(start_date='-5y').isoformat(),
        "is_active": fake.boolean(chance_of_getting_true=75),
        "address": fake.address().replace('\n', ', '),
        "phone_number": fake.phone_number()
    }
    users.append(user)

with open('users.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=users[0].keys())
    writer.writeheader()
    writer.writerows(users)

with open('users.json', 'w', encoding='utf-8') as f:
    json.dump(users, f, ensure_ascii=False, indent=2)
