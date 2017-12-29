#!/bin/bash
ID=$1
PASSWORD=$2
id_farmer=45203

#################
###token
#################
curl https://leekwars.com/api/farmer/login-token/$ID/$PASSWORD > mdp_leek.json
token=$(cat mdp_leek.json|jq -r ".token")

####################
###number of fights
####################

farmer=$(curl https://leekwars.com/api/farmer/get/$id_farmer)
echo $farmer
fights=$(echo $farmer|jq -r ".farmer")
number_fights=$(echo $fights|jq -r ".fights")

clear 
echo "number of fights " $number_fights

for i in `seq 1 $number_fights`;
do
	clear
	#curl https://leekwars.com/api/garden/get/$token
	curl https://leekwars.com/api/garden/get-farmer-opponents/$token >> garden.json
	cat garden.json|jq -r "[.opponents[]]">> enemy.json
	fighter=$(jq '.[].id' enemy.json|head -n 1)
	curl https://leekwars.com/api/garden/start-farmer-challenge/$fighter/$token >> result.json
	rm *.json
	sleep 20
done
