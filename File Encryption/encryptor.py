from cryptography.fernet import Fernet


# here we generate a key and write it in the same directory
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


# loading the key from the current directory
def load_key():
    return open("key.key", "rb").read()




def encrypt(filename, key):
    fern_encoder = Fernet(key)

    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()

    encrypted_data = fern_encoder.encrypt(file_data)
    with open (filename, 'wb') as file:

        file.write(encrypted_data)
    return  encrypted_data


def decrypt(filename, key):
    fern_encoder = Fernet(key)

    with open(filename, "rb") as file:
        # read all file data
        encrypted_data = file.read()
        decrypted_data = fern_encoder.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)
    return decrypted_data


data = 'data.txt'
key = load_key()

# encrypt(data, key)

decrypt(data, key)





