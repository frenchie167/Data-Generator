import uuid
import csv
import json
from datetime import datetime, timedelta
from random import choice, randint, random

first_names = ['John', 'Adam', 'Edward', 'Matthew', 'Bob']
last_names = ['Bryant', 'Bekker', 'Jones', 'Long', 'Brown']
domains = ['gmail.com', 'mail.ru', 'yandex.ru']

users = []
for _ in range(10000):
    users.append({
        "id": str(uuid.uuid4()),
        "first_name": choice(first_names),
        "last_name": choice(last_names),
        "email": f"{choice(first_names)}.{choice(last_names)}@example.com",
        "registration_date": (datetime.now() - timedelta(days=randint(0, 1000))).strftime("%Y-%m-%d"),
        "is_active": random() > 0.3,
        "address": f"ул. {choice(['Гришина', 'Кутузова', 'Поклонная'])}, д. {randint(1, 100)}",
        "phone_number": f"+7{randint(900,999)}{randint(1000000,9999999)}"
    })

with open('users.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=users[0].keys())
    writer.writeheader()
    writer.writerows(users)

with open('users.json', 'w', encoding='utf-8') as f:
    json.dump(users, f, ensure_ascii=False, indent=2)

print("Файлы users.csv и users.json созданы")