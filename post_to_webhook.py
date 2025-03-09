import os
import requests
from typing import Dict, Any

def send_pokemon_to_trmnl(pokemon_data: Dict[str, Any]) -> None:
    """Send Pokemon data to usetrmnl webhook."""
    webhook_url = os.environ["TRMNL_WEBHOOK_URL"]
    
    payload = {
        "merge_variables": {
            "pokemon_name": pokemon_data['name'],
            "pokemon_type": pokemon_data['types'],
            "pokemon_species": pokemon_data['species'],
            "pokemon_height": pokemon_data['height'],
            "pokemon_weight": pokemon_data['weight'],
            "pokemon_abilities": pokemon_data['abilities'],
            "pokemon_artwork": pokemon_data['artwork']
        }
    }
    
    response = requests.post(
        webhook_url,
        json=payload,
        headers={"Content-Type": "application/json"}
    )
    
    if response.status_code != 200:
        raise Exception(f"Failed to send data to webhook: {response.status_code}")
