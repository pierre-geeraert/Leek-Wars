from function_essential import readCredential,TokenLeekwars,revokeTokenLeekwars,source_api_address,writeInFile,request_api,test
from garden import getGardenForLeek,getSoloChallenge,getFarmerOpponents
import json
import time

PathCredential = "credential.txt"
leek_id = '49273'
id_leekwars_global = readCredential(PathCredential, "id")
password_leekwars_global = readCredential(PathCredential, "password")
token_global=TokenLeekwars(id_leekwars_global,password_leekwars_global)



# print(getFarmerOpponents(token_global))
# print(getSoloChallenge(leek_id,token_global))

tab=[1,2,3]
print(type(tab))

