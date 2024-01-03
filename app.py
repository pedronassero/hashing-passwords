import hashlib
import getpass
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def hashing_password(text):
    sha256 = hashlib.sha256()

    sha256.update(text.encode('utf-8'))

    hash_result = sha256.hexdigest()

    return hash_result

print("\033[91mWelcome to the Hashing System!\033[0m")
print("Please, complete your account.")

username = input("Username: ")
user_password = getpass.getpass("Password: ")

clear_terminal()
print("\033[92mAccount created succesfuly!\033[0m")

hash_result = hashing_password(user_password)
print("Your password has gone trough a hashing function.")

print("Would you like to see the hashed password or you want to try to login into our system?")
print("\033[96m1 - See your hashed password.\033[0m")
print("\033[96m2 - Login\033[0m")

option = input("Option: ")
if option == '1':
    clear_terminal()
    print(f'\033[91mHashed Password: {hash_result}\033[0m')
else:
    clear_terminal()
    login_username = input("Username: ")
    login_password = getpass.getpass("Password: ")
    login_hashed_password = hashing_password(login_password)
    if login_username == username and login_hashed_password == hash_result:
        print("\033[92mRight credentials!\033[0m") 
    else:
        print("\033[91mWrong credentials!\033[0m")




