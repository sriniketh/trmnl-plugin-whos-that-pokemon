import pytest
from unittest.mock import patch, Mock
from pokemon_api import fetch_random_pokemon

@pytest.fixture
def mock_pokemon_response():
    return {
        "name": "pikachu",
        "types": [{"type": {"name": "electric"}}],
        "species": {"name": "pikachu", "url": "https://pokeapi.co/api/v2/pokemon-species/25"},
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
    
@pytest.fixture
def mock_species_response():
    return {
        "name": "pikachu",
        "genera": [
            {
                "genus": "Souris Pokémon",
                "language": {"name": "fr"}
            },
            {
                "genus": "Mouse Pokémon",
                "language": {"name": "en"}
            }
        ]
    }

def test_fetch_random_pokemon_returns_correct_response(mock_pokemon_response, mock_species_response):
    with patch('requests.get') as mock_get:
        mock_get.side_effect = [
            Mock(json=lambda: mock_pokemon_response),
            Mock(json=lambda: mock_species_response)
        ]
        
        result = fetch_random_pokemon()
        
        assert result["name"] == "Pikachu"
        assert result["types"] == "electric"
        assert result["species"] == "Mouse Pokémon"
        assert result["height"] == "0.4 m"
        assert result["weight"] == "6.0 kg"
        assert result["abilities"] == "static, lightning-rod"
        assert result["artwork"] == "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png"

def test_fetch_random_pokemon_no_english_genus(mock_pokemon_response):
    species_response_no_english = {
        "name": "pikachu",
        "genera": [
            {
                "genus": "Souris Pokémon",
                "language": {"name": "fr"}
            }
        ]
    }
    
    with patch('requests.get') as mock_get:
        mock_get.side_effect = [
            Mock(json=lambda: mock_pokemon_response),
            Mock(json=lambda: species_response_no_english)
        ]
        
        result = fetch_random_pokemon()
        assert result["species"] == "pikachu"

def test_fetch_random_pokemon_calls_correct_endpoints(mock_pokemon_response, mock_species_response):
    with patch('requests.get') as mock_get, \
         patch('random.randint') as mock_randint:
        mock_get.side_effect = [
            Mock(json=lambda: mock_pokemon_response),
            Mock(json=lambda: mock_species_response)
        ]
        mock_randint.return_value = 25
        
        fetch_random_pokemon()
        
        mock_randint.assert_called_once_with(1, 1025)
        assert mock_get.call_count == 2
        mock_get.assert_any_call("https://pokeapi.co/api/v2/pokemon/25")
        mock_get.assert_any_call("https://pokeapi.co/api/v2/pokemon-species/25")

def test_fetch_random_pokemon_api_error():
    with patch('requests.get') as mock_get:
        mock_get.side_effect = Exception("API Error")
        
        with pytest.raises(Exception):
            fetch_random_pokemon()