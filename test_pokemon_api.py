import pytest
from unittest.mock import patch
from pokemon_api import fetch_random_pokemon

@pytest.fixture
def mock_pokemon_response():
    return {
        "name": "pikachu",
        "types": [{"type": {"name": "electric"}}],
        "species": {"name": "pikachu"},
        "height": 4,
        "weight": 60,
        "abilities": [
            {"ability": {"name": "static"}},
            {"ability": {"name": "lightning-rod"}}
        ],
        "sprites": {
            "other": {
                "official-artwork": {
                    "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png"
                }
            }
        }
    }

def test_fetch_random_pokemon(mock_pokemon_response):
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = mock_pokemon_response
        mock_get.return_value.status_code = 200
        
        result = fetch_random_pokemon()
        
        assert result["name"] == "Pikachu"
        assert result["types"] == "electric"
        assert result["species"] == "pikachu"
        assert result["height"] == "0.4 m"
        assert result["weight"] == "6.0 kg"
        assert result["abilities"] == "static, lightning-rod"
        assert result["artwork"] == "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png"

def test_fetch_random_pokemon_random_id():
    with patch('requests.get') as mock_get, \
         patch('random.randint') as mock_randint:
        mock_randint.return_value = 25
        mock_get.return_value.status_code = 200
        
        fetch_random_pokemon()
        
        mock_randint.assert_called_once_with(1, 1025)
        mock_get.assert_called_once_with("https://pokeapi.co/api/v2/pokemon/25")

def test_fetch_random_pokemon_api_error():
    with patch('requests.get') as mock_get:
        mock_get.side_effect = Exception("API Error")
        
        with pytest.raises(Exception):
            fetch_random_pokemon()