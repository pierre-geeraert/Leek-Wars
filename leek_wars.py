from function_essential import readCredential,TokenLeekwars
from garden import GetGardenForLeek,getSoloChallenge

PathCredential = "credential.txt"
leek_id = '49273'

id_leekwars_global = readCredential(PathCredential, "id")
password_leekwars_global = readCredential(PathCredential, "password")
token_global=TokenLeekwars(id_leekwars_global,password_leekwars_global)

#print(getSoloChallenge(leek_id,token_global))
print(GetGardenForLeek(leek_id,token_global))

