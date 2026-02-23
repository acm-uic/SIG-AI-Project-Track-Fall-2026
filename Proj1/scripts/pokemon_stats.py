import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon_stats(pokemon_name):
    url = f"{BASE_URL}{pokemon_name.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
        return stats
    
    else:
        print(f"Error: Could not retrieve data for {pokemon_name}. Status code: {response.status_code}")
        return None
    

if __name__ == "__main__":

    pokemon_name = input("Enter the name of the Pokémon (for Hisuian variants, add '-hisui'): ")

    stats = get_pokemon_stats(pokemon_name)
    
    if stats:
        print(f"Stats for {pokemon_name.capitalize()}:")
        for stat_name, stat_value in stats.items():
            print(f"{stat_name.capitalize()}: {stat_value}")