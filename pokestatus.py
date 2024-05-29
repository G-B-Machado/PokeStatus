import csv
import pandas as pd

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

def transform_dict_to_list(dict):
    list_pokemons = list(dict.values())
    return list_pokemons
    
def get_pokemons_by_generation(list, generation):
    generation_list = []
    for pokemon in list:
        if pokemon[10] == generation:
            generation_list.append(pokemon[0])
    return generation_list

def get_legendary_pokemons(list, legendary):
    legendary_list = []
    for pokemon in list:
        if pokemon[11] == legendary:
            legendary_list.append(pokemon[0])
    return legendary_list

def get_pokemons_pandas():
    df = pd.read_csv("pokemon.csv")
    print(df.head(2))
    #print(df.info())
    print(df[df.Name=='Charmander'])
    # using | (or) & (and)
    print(df[(df['Type 1']=='Grass') & (df.Generation == 1)])
    df_pyschic_pokemons = df[(df.Generation.isin([1,3,4])) & (df["Type 1"]=='Psychic')]
    df.reset_index(drop = True)
    print(df_pyschic_pokemons)
    #add column
    df['New Column'] = 'Teste'
    df['Total Attack'] = df.Attack + df['Sp. Atk']
    df['Upper Name'] = df.Name.apply(str.upper)
    
    get_last_name = lambda x: x.split()[-1]
    df['last_name'] = df.Name.apply(get_last_name)

    '''
    total_earned = lambda row: (row.hourly_wage * 40) + ((row.hourly_wage * 1.5) * (row.hours_worked - 40)) \
	if row.hours_worked > 40 \
    else row.hourly_wage * row.hours_worked
  
    df['total_earned'] = df.apply(total_earned, axis = 1)
    '''
    '''0if I use .columns in the current Data Frame, I can change all the columns name. 
        exp: df.columns = [..., 'Type_1', 'Type_2', 'Sp._atk', ...]
    '''

    df.rename(columns = {'Type 1': 'Type_1', 'Type 2': 'Type_2'}, inplace=True)

    print(df.head(2))

def main():

    get_pokemons_pandas()

    '''
    pokemons = get_pokemons()
    pokemon_list = transform_dict_to_list(pokemons)
    generation_list = []

    print(f"We have {len(pokemons)} pokemons")

    id = input("Please, insert a pokemon id: ")
    print(search_pokemon_by_id(pokemons, id))

    pokemon_types = input("Input a pokemon type: ")
    search_pokemon_by_type(pokemons, pokemon_types)

    generation = input("Input a generation: ")
    generation_list = get_pokemons_by_generation(pokemon_list, generation)
    print(generation_list)

    print(get_legendary_pokemons(pokemon_list, "True"))
    '''

if __name__ == "__main__":
    main()