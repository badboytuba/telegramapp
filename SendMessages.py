from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError
import sys
import csv
import random
import time


api_id = 25423946   #Enter Your 7 Digit Telegram API ID.
api_hash = '8f0ac65b3d4675bea70c177a8a17d0a5'   #Enter Yor 32 Character API Hash.
phone = '34613987159'   #Enter Your Mobilr Number With Country Code.
client = TelegramClient(phone, api_id, api_hash)

SLEEP_TIME_2 = 600
SLEEP_TIME_1 = 300
SLEEP_TIME = 150
client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))



users = []
with open(r"Scrapped.csv", encoding='UTF-8') as f:
    rows = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rows, None)
    for row in rows:
        user = {}
        user['username'] = row[0]
        user['id'] = int(row[1])
        user['access_hash'] = int(row[2])
        user['name'] = row[3]
        users.append(user)

mode = int(input("Enter 1 to send by user ID or 2 to send by username: "))

#Enter you message here!
messages= ["""OLA {}, Trader, 

Vou lhe Apresentar uma Plataforma de Analises de Jogos e Trips com Algoritmos que Possui mais de +10 Filtros Prontos com mais de 77% de Greem em Gols HT/FT, Cornes HT/FT, e Resultados HT/FT,

A Plataforma Também Permite que você Crie Seus Próprios Robôs e Receber as Trips Via Telegram, Conforme sua Experiência de Jogo, 

Analisando inúmeros dados pré jogo e ao vivo. 

Simples Assim, fácil e Tudo em Português.

Planos Acessíveis e Suporte Prioritário.

Acesso ao Site para Saber Mais...

Site: https://kiwify.app/0lfx4lJ?afid=LquQfEsM"""]
for user in users:
    if mode == 2:
        if user['username'] == "":
            continue
        receiver = client.get_input_entity(user['username'])
    elif mode == 1:
        receiver = InputPeerUser(user['id'],user['access_hash'])
    else:
        print("Invalid Mode. Exiting.")
        client.disconnect()
        sys.exit()
    message = random.choice(messages)
    try:
        print("Sending Message to:", user['name'])
        client.send_message(receiver, message.format(user['name']))
        print("Waiting {} seconds".format(SLEEP_TIME))
        time.sleep(SLEEP_TIME)
    except PeerFloodError:
        print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
        print("Waiting {} seconds".format(SLEEP_TIME_2))
        time.sleep(SLEEP_TIME_2)
    except Exception as e:
        print("Error:", e)
        print("Trying to continue...")
        print("Waiting {} seconds".format(SLEEP_TIME_1))
        time.sleep(SLEEP_TIME_1)
client.disconnect()
print("Done. Message sent to all users.")
