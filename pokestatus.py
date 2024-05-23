import csv
def get_pokemons():
    dict_pokemons = {}
    with open("pokemon.csv","r") as pokemon_file:
        pokemons = csv.reader(pokemon_file)
        next(pokemons)

        for pokemon in pokemons:            
            dict_pokemons[pokemon[0]] = pokemon[1:]

    return dict_pokemons

def search_pokemon_by_id(dict, id):
    if id in dict:
        return dict[id]
    else:
        print("Pokemon not found")

def search_pokemon_by_type(dict, type):
    list_pokemons = list(dict.values())
    list_type_pokemons = []
    for pokemon in list_pokemons:
        if pokemon[1] == type:
            list_type_pokemons.append(pokemon)
    print(f"There are {len(list_type_pokemons)} {type} type pokemons")  


def main():
    pokemons = get_pokemons()
    print(f"We have {len(pokemons)} pokemons")
    id = input("Please, insert a pokemon id: ")
    pokemon_types = input("Input a pokemon type: ")
    print(search_pokemon_by_id(pokemons, id))
    search_pokemon_by_type(pokemons, pokemon_types)
    
if __name__ == "__main__":
    main()