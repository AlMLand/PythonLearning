# for storing of key-value items
customer = {
    "id": 1,
    "name": "Some Name ",
    "phone": "123-456",
    "premiumMember": True,
    "score": 2.3
}

print(customer.get("id"))
print(customer["id"])

customers = [
    {
        "id": 1,
        "name": "Some Name 1",
        "phone": "123-456",
        "premiumMember": True,
        "score": 2.3
    },
    {
        "id": 2,
        "name": "Some Name 2",
        "phone": "789-000",
        "premiumMember": False,
        "score": 4.5
    }
]

for customer in customers:
    for k, v in customer.items():
        print(f"{k} - {v}")
