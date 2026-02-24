import requests
import pandas as pd
import pathlib


BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon_stats(pokemon_name):
    url = f"{BASE_URL}{pokemon_name.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
        types = {type['type']['name'] for type in data['types']}
        return stats, tuple(types)
    
    else:
        print(f"Error: Could not retrieve data for {pokemon_name}. Status code: {response.status_code}")
        return None

if __name__ == "__main__":

    # Data Folder: ../data
    data_folder = pathlib.Path("../data")
    if not data_folder.exists():
        data_folder.mkdir()


    # Create dataframe
    pokemon_name = input("Enter the name of the Pokémon (for Hisuian variants, add '-hisui'): ")

    stats, types = get_pokemon_stats(pokemon_name)

    stats['type1'] = types[0]

    try:
        stats['type2'] = types[1]
    except IndexError:
        stats['type2'] = None
    
    df = pd.DataFrame(stats, index=[pokemon_name])
    print(df)

    # Save to CSV
    csv_path_string = data_folder + "/poke_stats.csv"
    df.to_csv(csv_path)
    print(f"{csv_path} saved!")
    