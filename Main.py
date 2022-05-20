import CreateAccount
import YesPlease
# import CreateAccountDetails
from faker import Faker
fake = Faker(['en_IN'])

print("Fill all Details for creating account")


# firstName = str(input("First Name "))
# lastName = str(input("Last Name "))
# phoneNumber = str(input("Phone Number "))
# emailAddress = str(input("Email Address "))
# Password = str(input("Password "))

for i in range(1):
    firstName = fake.first_name()
    lastName = fake.last_name()
    phoneNumber = "0865565656"
    emailAddress = fake.email()
    Password = "Root@123"

    CreateAccount.CreateAccount(firstName, lastName,phoneNumber, emailAddress, Password)
    YesPlease.YesPlease(emailAddress, Password)
  
# YesPlease.YesPlease(emailAddress,Password)    
