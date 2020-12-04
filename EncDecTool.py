from cryptography.fernet import Fernet
from colorama import Fore, Style, Back
import os
from binascii import Error
from cryptography import *
import cryptography
import binascii

def run(runfile):
	with open(runfile,"r") as rnf:
		exec(rnf.read())

def key_generat():
    os.system("clear")
    print(Style.BRIGHT + Fore.YELLOW + """
    [1] Generate Key Options""")
    key = Fernet.generate_key()
    key_name = input("""
    Enter Key Name : """)
    file = open(key_name + ".key", "wb")
    file.write(key)
    file.close()
    print("""
    Key Generated Successfully""")
    print("""
    Output File Name >>> """ + key_name + ".key\n")
    print(Style.RESET_ALL)
    run("EncDecTool.py")

def encrypt_file():
    os.system("clear")
    print(Style.BRIGHT + Fore.MAGENTA + """
    [2] Encrypt File Options""")
    try:
        key_file = input("""
    Enter Your Key File : """)
        file = open(key_file + ".key", "rb")
        key = file.read()
        file.close()

        your_enc_file = input("""
    Choose Your Encrypt File : """)
        
        with open (your_enc_file, "rb") as f:
            data = f.read()

        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)

        with open (your_enc_file, "wb") as f:
            f.write(encrypted)
            print("""
    Encryption Successfully\n""")
            run("EncDecTool.py")
    
    except FileNotFoundError:
        print("""
    File Not Found !\n""")
    print(Style.RESET_ALL)
    run("EncDecTool.py")

def decrypt_file():
    os.system("clear")
    print(Style.BRIGHT + Fore.GREEN + """
    [3] Decrypt File Options""")

    try:    
        key_file = input("""
    Enter Your Key File : """)
        file = open(key_file + ".key", "rb")
        key = file.read()
        file.close()
        your_decrypt_file = input("""
    Choose Your Decrypt File : """)
        with open (your_decrypt_file, "rb") as f:
            data = f.read()
        
        try:
            fernet=Fernet(key)
            encrypted = fernet.decrypt(data)
        except (cryptography.fernet.InvalidToken, TypeError, UnboundLocalError, Error):
            print("""
    Key File Or Encrypt File Not Correct ! Try Again\n""")
            run("EncDecTool.py")

        with open (your_decrypt_file, "wb") as f:
            f.write(encrypted)
            print("""
    Decryption Successfully\n""")
            run("EncDecTool.py")
    
    except FileNotFoundError:
        print("""
    File Not Found !\n""" + Style.RESET_ALL)
        run("EncDecTool.py")

print(Style.BRIGHT + Fore.GREEN + """
       ____                       __    ____      ___                        __    _____ __   
      / __/__  __________ _____  / /_  / __/___  / _ \___ __________ _____  / /_  / __(_) /__ 
     / _// _ \/ __/ __/ // / _ \/ __/  > _/_ _/ / // / -_) __/ __/ // / _ \/ __/ / _// / / -_)
    /___/_//_/\__/_/  \_, / .__/\__/  |_____/  /____/\__/\__/_/  \_, / .__/\__/ /_/ /_/_/\__/ 
                    /___/_/                                    /___/_/                       
                                Code By : Aung Thu Myint""" + Style.BRIGHT + Fore.CYAN + """

        [1] Generate Key
        
        [2] Encrypt File
        
        [3] Decrypt File
        
        [4] Exit""" + Style.RESET_ALL)

print(Style.BRIGHT + Fore.BLUE)
enter_options = str(input("""
    Enter Your Options : """))

if enter_options==str(1):
    key_generat()

elif enter_options==str(2):
    encrypt_file()

elif enter_options==str(3):
    decrypt_file()

elif enter_options==str(4):
    print(Style.BRIGHT + Fore.RED + """
    Bye Bye ... !\n""" + Style.RESET_ALL)
    exit()

else:
    os.system("clear")
    print(Style.BRIGHT + Fore.RED + """
    Incorrect Options ! Try Again\n""" + Style.RESET_ALL)
    run("EncDecTool.py")