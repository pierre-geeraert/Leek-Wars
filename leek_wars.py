from function_essential import readCredential,TokenLeekwars,revokeTokenLeekwars,source_api_address,writeInFile,request_api,test
from garden import getGardenForLeek,getSoloChallenge,getFarmerOpponents
import json
import time

PathCredential = "credential.txt"
leek_id = '49273'
id_leekwars_global = readCredential(PathCredential, "id")
password_leekwars_global = readCredential(PathCredential, "password")
token_global=TokenLeekwars(id_leekwars_global,password_leekwars_global)


# opponents1 = ""
# opponents2 = ""
# opponents3 = ""
# opponents4 = ""
# opponents5 = ""
# data_out = ""

data_out,opponents1,opponents2,opponents3,opponents4,opponents5 = getFarmerOpponents(token_global)
print(data_out)
print(opponents1)
print(opponents2)
print(opponents3)
print(opponents4)
print(opponents5)
#print(getFarmerOpponents(token_global))
