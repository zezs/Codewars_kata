from cryptography.fernet import Fernet

master_pwd = input("Enter a master password")

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

while True:
    choice = int(input("Menu 1.Add  2.View  3.Quit: "))

    if choice == 1:
        name = input("Enter name: ")
        pwd = input("Enter pwd: ")

        with open("info.txt", "a") as f: 
            f.write(name + "|" + pwd + "\n")

    elif choice == 2:
        
        with open("info.txt", "r") as f:
            for line in f.readlines():
                data = line.rstrip()
                name, pwd = data.split("|") 
                print("User:", name, "Password:", pwd)

    elif choice == 3:
        quit()

    else: 
        print("Invalid Input")

