import csv
def get_pokemons():
    dict_pokemons = {}
    with open("pokemon.csv","r") as pokemon_file:
        pokemons = csv.reader(pokemon_file)
        next(pokemons)

        for pokemon in pokemons:            
            dict_pokemons[pokemon[0]] = pokemon[1:]

    return dict_pokemons


def main():
    pokemons = get_pokemons()
    print(pokemons)
    
if __name__ == "__main__":
    main()