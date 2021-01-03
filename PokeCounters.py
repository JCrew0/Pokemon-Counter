import requests
from requests.exceptions import HTTPError

pokemon = raw_input("Enter the name of the Pokemon you're looking for: ").lower()

ROOT_URL = "https://pokeapi.co/api/v2/"

POKE_URL = ROOT_URL + "pokemon/" + pokemon

ROOT_TYPE_URL = ROOT_URL + "type/"


def process_data(data):
    poketypes = data['types']

    print(pokemon.capitalize() + ' is type(s):'),

    for ty in poketypes:
        print(ty['type']['name'].capitalize()),

    print

    print(pokemon.capitalize() + " does double damage to pokemon of type(s):"),

    for ty in poketypes:
        temptype = ty['type']['name']
        tempurl = ROOT_TYPE_URL + temptype
        tempresponse = requests.get(tempurl).json()
        countertypes = tempresponse['damage_relations']['double_damage_to']
        for i in countertypes:
            print(i['name'].capitalize()),

    print
    print(pokemon.capitalize() + " does half damage to pokemon of type(s):"),

    for ty in poketypes:
        temptype = ty['type']['name']
        tempurl = ROOT_TYPE_URL + temptype
        tempresponse = requests.get(tempurl).json()
        countertypes = tempresponse['damage_relations']['half_damage_to']
        for i in countertypes:
            print(i['name'].capitalize()),

    print
    print(pokemon.capitalize() + " receives double damage to pokemon of type(s):"),

    for ty in poketypes:
        temptype = ty['type']['name']
        tempurl = ROOT_TYPE_URL + temptype
        tempresponse = requests.get(tempurl).json()
        countertypes = tempresponse['damage_relations']['double_damage_from']
        for i in countertypes:
            print(i['name'].capitalize()),

    print
    print(pokemon.capitalize() + " does half damage to pokemon of type(s):"),

    for ty in poketypes:
        temptype = ty['type']['name']
        tempurl = ROOT_TYPE_URL + temptype
        tempresponse = requests.get(tempurl).json()
        countertypes = tempresponse['damage_relations']['half_damage_from']
        for i in countertypes:
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
        print('Something went wrong. Please try again and make sure the name you entered is correct.')