from pipenv.utils import requests
from globalVar import header
from function_essential import request_api,source_api_address

def makeFight(leek_id,target_id):
    data_out_makeFight = requests.get("https://leekwars.com/api/garden/start-solo-fight/" + str(leek_id) + "/" + str(target_id),headers=header)
    return data_out_makeFight.content.decode('utf-8')

def nbrFightAvailable():
    try:
        data_out_nbrFightAvailable = request_api(source_api_address + "garden/get")['garden']['fights']
    except:
        print("request impossible for nbrFightAvailable")
    return data_out_nbrFightAvailable