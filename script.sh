#!/bin/bash
ID=$1
PASSWORD=$2
id_farmer=45203
id_leek=49273
#################
###token
#################
curl https://leekwars.com/api/farmer/login-token/$ID/$PASSWORD > mdp_leek.json
token=$(cat mdp_leek.json|jq -r ".token")

####################
###number of fights
####################

farmer=$(curl https://leekwars.com/api/farmer/get/$id_farmer)
#echo $farmer
fights=$(echo $farmer|jq -r ".farmer")
number_fights=$(echo $fights|jq -r ".fights")

clear 
echo "number of fights " $number_fights
sleep 3
for i in `seq 1 $number_fights`;
do
	clear
	curl https://leekwars.com/api/garden/get-leek-opponents/$id_leek/$token > garden.json
	cat garden.json|jq -r "[.opponents[]]"> enemy.json
	#fighter=$(jq '.[].id' enemy.json|head -n 1)
	fighter=$(cat enemy.json | jq '.['$(./talent.sh)'].id')
	clear
	firefox https://leekwars.com/api/garden/start-solo-fight/$id_leek/$fighter/$token > result.json
	firefox https://leekwars.com/garden/solo
	rm *.json
	clear
	echo "wait 15 seconds"
	sleep 15
done
clear
echo "fin des combats"
killall firefox
