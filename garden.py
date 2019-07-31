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
    except:
        print("request impossible for getFarmerOpponents")
    return data_out_getFarmerOpponents