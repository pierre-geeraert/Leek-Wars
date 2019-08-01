from pipenv.utils import requests
from globalVar import header

def makeFight(leek_id,target_id):
    data_out_makeFight = requests.get("https://leekwars.com/api/garden/start-solo-fight/" + str(leek_id) + "/" + str(target_id),headers=header)
    return data_out_makeFight.content.decode('utf-8')

def nbrFightAvailable(token):
    return 0