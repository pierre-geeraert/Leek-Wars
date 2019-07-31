from function_essential import request_api
import function_essential
source_api_address=function_essential.source_api_address+"garden/"

def getGardenForLeek(leek_id, token):
    try:
        data_out_GetGardenForLeek = request_api(source_api_address + "get-leek-opponents/" + leek_id, token)
    except:
        print("request impossible for GetGardenForLeek")
    return data_out_GetGardenForLeek


def getSoloChallenge(leek_id, token):
    try:
        data_out_getSoloChallenge = request_api(source_api_address + "get-solo-challenge/" + leek_id,token)
    except:
        print("request impossible for GetGardenForLeek")
    return data_out_getSoloChallenge

def getFarmerOpponents(token):
    try:
        data_out_getFarmerOpponents = request_api(source_api_address+"get-farmer-opponents",token)
        tab_opponents = data_out_getFarmerOpponents['opponents']
        opponents1 = tab_opponents[0]
        opponents2 = tab_opponents[1]
        opponents3 = tab_opponents[2]
        opponents4 = tab_opponents[3]
        opponents5 = tab_opponents[4]

    except:
        print("request impossible for getFarmerOpponents")
    return data_out_getFarmerOpponents,opponents1,opponents2,opponents3,opponents4,opponents5