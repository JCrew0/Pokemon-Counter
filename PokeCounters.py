# Author: Justin Carway
# Last Updated: 01/03/21
# Description: This file will take in the name of a pokemon and then output the type of that pokemon as well as what it
# is weak/strong against. It uses the requests library to ping the api at https://pokeapi.co/ and receive the associated
# JSON. Exception handling is relatively minimal at the moment, but the file works at a basic level.

import requests
from requests.exceptions import HTTPError

# depending on how this file is being run, this line may need to be changed from "raw_input" to "input"
pokemon = raw_input("Enter the name of the Pokemon you're looking for: ").lower()

ROOT_URL = "https://pokeapi.co/api/v2/"  # overall root url
POKE_URL = ROOT_URL + "pokemon/" + pokemon  # url for the given pokemon
ROOT_TYPE_URL = ROOT_URL + "type/"  # url for any type


# This function takes in a JSON object for a particular pokemon, it then prints of the types of that pokemon as well as
# the types that pokemon is strong/weak against
def process_data(data):
    poke_types = data['types']  # getting the types of the pokemon

    # transversing through and printing the types of the given pokemon
    print(pokemon.capitalize() + ' is type(s):'),
    for ty in poke_types:
        print(ty['type']['name'].capitalize()),

    print

    # transversing through and printing the types the given pokemon does double damage to
    print(pokemon.capitalize() + " does double damage to pokemon of type(s):"),
    for ty in poke_types:
        temp_type = ty['type']['name']
        temp_url = ROOT_TYPE_URL + temp_type
        temp_response = requests.get(temp_url).json()
        counter_types = temp_response['damage_relations']['double_damage_to']
        for i in counter_types:
            print(i['name'].capitalize()),

    print

    # transversing through and printing the types the given pokemon does half damage to
    print(pokemon.capitalize() + " does half damage to pokemon of type(s):"),
    for ty in poke_types:
        temp_type = ty['type']['name']
        temp_url = ROOT_TYPE_URL + temp_type
        temp_response = requests.get(temp_url).json()
        counter_types = temp_response['damage_relations']['half_damage_to']
        for i in counter_types:
            print(i['name'].capitalize()),

    print

    # transversing through and printing the types the given pokemon takes double damage from
    print(pokemon.capitalize() + " receives double damage to pokemon of type(s):"),
    for ty in poke_types:
        temp_type = ty['type']['name']
        temp_url = ROOT_TYPE_URL + temp_type
        temp_response = requests.get(temp_url).json()
        counter_types = temp_response['damage_relations']['double_damage_from']
        for i in counter_types:
            print(i['name'].capitalize()),

    print

    # transversing through and printing the types the given pokemon takes half damage from
    print(pokemon.capitalize() + " does half damage to pokemon of type(s):"),
    for ty in poke_types:
        temp_type = ty['type']['name']
        temp_url = ROOT_TYPE_URL + temp_type
        temp_response = requests.get(temp_url).json()
        counter_types = temp_response['damage_relations']['half_damage_from']
        for i in counter_types:
            print(i['name'].capitalize()),


# main
if __name__ == '__main__':

    try:
        # Retrieving the data
        response = requests.get(POKE_URL).json()
        process_data(response)

    except HTTPError as http_err:
        print('Something went wrong. Please try again and make sure the name you entered is correct.')
    except Exception as err:
        print('Something went wrong. Please try again.')
