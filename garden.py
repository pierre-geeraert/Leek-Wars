from function_essential import request_api
from function_essential import source_api_address



def GetGardenForLeek(leek_id, token):
    try:
        data_out_GetGardenForLeek = request_api(source_api_address + "garden/get-leek-opponents/" + leek_id, token)
    except:
        print("request impossible for GetGardenForLeek")
    return data_out_GetGardenForLeek


def getSoloChallenge(leek_id, token):
    try:
        data_out_getSoloChallenge = request_api(source_api_address + "garden/get-solo-challenge/" + leek_id,token)
    except:
        print("request impossible for GetGardenForLeek")
    return data_out_getSoloChallenge
