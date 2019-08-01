from random import randint

from pipenv.utils import requests

import globalVar
from function_essential import request_api
import function_essential
import json
source_api_address=function_essential.source_api_address+"garden/"


def getGardenForLeek(leek_id):
    try:
        data_out_GetGardenForLeek = request_api(source_api_address + "get-leek-opponents/" + leek_id)
    except:
        print("request impossible for GetGardenForLeek")
    return data_out_GetGardenForLeek


def getSoloChallenge(leek_id):
    try:
        data_out_getSoloChallenge = request_api(source_api_address + "get-solo-challenge/" + leek_id)
    except:
        print("request impossible for GetGardenForLeek")
    return data_out_getSoloChallenge

def getAI():
    try:
        data_out_getAI = request_api(function_essential.source_api_address + "ai/get-farmer-ais")
    except:
        print("request impossible for getAI")
    return data_out_getAI

def getLeekOpponents(leek_id):
    try:
        data_out_getFarmerOpponents = request_api(source_api_address+"get-leek-opponents/"+leek_id)
        tab_opponents = data_out_getFarmerOpponents['opponents']
        opponents1 = tab_opponents[0]
        opponents2 = tab_opponents[1]
        opponents3 = tab_opponents[2]
        opponents4 = tab_opponents[3]
        opponents5 = tab_opponents[4]

    except:
        print("request impossible for getLeekOpponents")
        data_out_getFarmerOpponents,opponents1,opponents2,opponents3,opponents4,opponents5 = "error"

    return opponents1,opponents2,opponents3,opponents4,opponents5

def theBaddestOpponents():
    opponents1 = ""
    opponents2 = ""
    opponents3 = ""
    opponents4 = ""
    opponents5 = ""
    opponents1,opponents2,opponents3,opponents4,opponents5 = getLeekOpponents(globalVar.leek_id)
    data_out_theBaddestOpponents = baddestOpponents(opponents1,opponents2,opponents3,opponents4,opponents5)
    return data_out_theBaddestOpponents


def baddestOpponents(opponents1,opponents2,opponents3,opponents4,opponents5):
    global baddest_talent
    baddest_talent = 1000000
    global baddest_talent_opponents
    for opponents in opponents1,opponents2,opponents3,opponents4,opponents5:
        if opponents['talent'] <  baddest_talent:
            baddest_talent = opponents['talent']
            baddest_talent_opponents = opponents




    return baddest_talent_opponents

def bestOpponents(opponents1,opponents2,opponents3,opponents4,opponents5):
    global best_talent
    best_talent=0
    global best_talent_opponents
    for opponents in opponents1,opponents2,opponents3,opponents4,opponents5:
        if opponents['talent'] >  best_talent:
            best_talent = opponents['talent']
            best_talent_opponents = opponents

    return best_talent_opponents