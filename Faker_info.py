from asyncore import write
from faker import Faker
fake = Faker(['en_IN'])

# 'Lucy Cechtelar'
for i in range(1000):
    print("===============================")
    print("Name ", fake.name())
    print("Email ", fake.email())
    print("Address ", fake.address())
    print("phone Number ", fake.phone_number())
    print("Name "+fake.name())

