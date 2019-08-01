from random import randint
from function_essential import TokenLeekwars, readCredential

PathCredential = "credential.txt"
leek_id = '57610'
id_leekwars_global = readCredential(PathCredential, "id")
password_leekwars_global = readCredential(PathCredential, "password")

token_global=TokenLeekwars(id_leekwars_global,password_leekwars_global)


header = {'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token_global),
                  "Cookie": "PHPSESSID=" + str(randint(0, 1000))};