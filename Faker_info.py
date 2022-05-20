from faker import Faker
fake = Faker(['en_IN'])

file = open("Faker.txt", "a")
# 'Lucy Cechtelar'
for i in range(100000000):
    # print("===============================")
    # print("Name ", fake.name())
    # print("Email ", fake.email())
    # print("Address ", fake.address())
    # print("phone Number ", fake.phone_number())
    file.write("===============================\n")
    file.write("Name "+fake.name()+"\n")
    file.write("Email "+fake.email()+"\n")
    file.write("Address "+fake.address()+"\n")
    file.write("phone Number "+fake.phone_number()+"\n")

# print(file.read())