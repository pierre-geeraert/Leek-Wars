from function_essential import readCredential,TokenLeekwars,revokeTokenLeekwars,source_api_address,writeInFile,request_api
from garden import GetGardenForLeek,getSoloChallenge
import json

PathCredential = "credential.txt"
leek_id = '49273'

id_leekwars_global = readCredential(PathCredential, "id")
password_leekwars_global = readCredential(PathCredential, "password")
token_global=TokenLeekwars(id_leekwars_global,password_leekwars_global)


id_leek=request_api(source_api_address+"farmer/login-token"+"/"+id_leekwars_global+"/"+password_leekwars_global,token_global)
#print(id_leek)
print(id_leek["farmer"]["leeks"])