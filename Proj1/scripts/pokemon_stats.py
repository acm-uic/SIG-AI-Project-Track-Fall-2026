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
    
<<<<<<< HEAD
    df = pd.DataFrame(stats, index=[pokemon_name])
    print(df)

    # Save to CSV
    csv_path_string = data_folder + "/poke_stats.csv"
    df.to_csv(csv_path)
    print(f"{csv_path} saved!")
    
=======
    if stats:
        print(f"Stats for {pokemon_name.capitalize()}:")
        for stat_name, stat_value in stats.items():
            print(f"{stat_name.capitalize()}: {stat_value}")













# def get_json(url):
#     return requests.get(url).json()

# def get_fully_evolved_pokemon(limit=1025):
#     fully_evolved = []

#     for i in range(1, limit + 1):
#         pokemon = get_json(f"{BASE_URL}/pokemon/{i}")
#         species = get_json(pokemon["species"]["url"])
#         evo_chain = get_json(species["evolution_chain"]["url"])

#         def find_in_chain(chain):
#             if chain["species"]["name"] == pokemon["name"]:
#                 return chain
#             for evo in chain["evolves_to"]:
#                 found = find_in_chain(evo)
#                 if found:
#                     return found
#             return None

#         node = find_in_chain(evo_chain["chain"])

#         if node and len(node["evolves_to"]) == 0:
#             stats = {stat["stat"]["name"]: stat["base_stat"] for stat in pokemon["stats"]}
#             fully_evolved.append({
#                 "name": pokemon["name"],
#                 **stats
#             })

#         time.sleep(0.2)  # be polite to API

#     return fully_evolved

>>>>>>> f7a689d (Done)
