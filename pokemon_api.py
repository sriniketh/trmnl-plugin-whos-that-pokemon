import random
import requests
from typing import Dict, Any

__MAX_POKEMON_ID = 1025

def fetch_random_pokemon() -> Dict[str, Any]:
    """Fetch random Pokemon data from PokeAPI."""
    pokemon_id = random.randint(1, __MAX_POKEMON_ID)
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    pokemon_data = response.json()

    types = [t["type"]["name"] for t in pokemon_data["types"]]
    abilities = [a["ability"]["name"] for a in pokemon_data["abilities"]]
    
    species_url = pokemon_data["species"]["url"]
    species_response = requests.get(species_url)
    species_data = species_response.json()
    
    for genus in species_data["genera"]:
        if genus["language"]["name"] == "en":
            species_name = genus["genus"]
            break
    else:
        species_name = species_data["name"]
    
    return {
        "name": pokemon_data["name"].title(),
        "types": ", ".join(type.title() for type in types),
        "species": species_name.title(),
        "height": f"{pokemon_data["height"] / 10} m",  # Convert to meters
        "weight": f"{pokemon_data["weight"] / 10} kg",  # Convert to kilograms
        "abilities": ", ".join(ability.title() for ability in abilities),
        "artwork": pokemon_data["sprites"]["other"]["official-artwork"]["front_default"]
    }
