#!/bin/bash
for i in `seq 1 100`;
do
	clear
	curl https://leekwars.com/api/farmer/login-token/ID/PASSWORD > mdp_leek.json
	token=$(cat mdp_leek.json|jq -r ".token") 
	#curl https://leekwars.com/api/garden/get/$token
	curl https://leekwars.com/api/garden/get-farmer-opponents/$token >> garden.json
	cat garden.json|jq -r "[.opponents[]]">> enemy.json
	fighter=$(jq '.[].id' enemy.json|head -n 1)
	#echo $fighter
	curl https://leekwars.com/api/garden/start-farmer-challenge/$fighter/$token >> result.json
	rm *.json
	sleep 20
done
