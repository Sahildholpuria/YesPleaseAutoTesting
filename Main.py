import CreateAccount
import YesPlease


firstName = str(input("First Name "))
lastName = str(input("Last Name "))
phoneNumber = str(input("Phone Number "))
emailAddress = str(input("Email Address "))
Password = str(input("Password "))

CreateAccount.CreateAccount(firstName, lastName, phoneNumber, emailAddress, Password)
  
YesPlease.YesPlease(emailAddress,Password)    