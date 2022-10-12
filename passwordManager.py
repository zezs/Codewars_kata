from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input(" what is the master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open('pass.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            name, pwd = data.split("|")
            print("User: ", name, "| Password: ", str(fer.decrypt(pwd.encode())) + '\n')

def add():
    name = input("Account name: ")
    pwd  = input("Password: ")

    with open('pass.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.decode()) + '\n')
   

while True:
    mode = input("Would you like to add a new password or input a new one? (view/ add)").lower()

    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid password")
        continue
