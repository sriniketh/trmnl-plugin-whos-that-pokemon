import pytest
import requests
from unittest.mock import patch, Mock
from post_to_webhook import send_pokemon_to_trmnl

@pytest.fixture
def sample_pokemon_data():
    return {
        "name": "Pikachu",
        "types": "electric",
        "species": "mouse",
        "height": "0.4 m",
        "weight": "6.0 kg",
        "abilities": "static, lightning-rod",
        "artwork": "https://example.com/pikachu.png"
    }

@pytest.fixture
def mock_env_webhook_url(monkeypatch):
    monkeypatch.setenv("TRMNL_WEBHOOK_URL", "https://api.test.webhook/endpoint")

def test_send_pokemon_to_trmnl_success(sample_pokemon_data, mock_env_webhook_url):
    with patch('requests.post') as mock_post:
        mock_post.return_value = Mock(status_code=200)
        
        send_pokemon_to_trmnl(sample_pokemon_data)
        
        mock_post.assert_called_once()
        
        call_args = mock_post.call_args
        assert call_args[0][0] == "https://api.test.webhook/endpoint"
        
        payload = call_args[1]['json']
        assert 'merge_variables' in payload
        
        merge_vars = payload['merge_variables']
        assert merge_vars['pokemon_name'] == "Pikachu"
        assert merge_vars['pokemon_type'] == "electric"
        assert merge_vars['pokemon_species'] == "mouse"
        assert merge_vars['pokemon_height'] == "0.4 m"
        assert merge_vars['pokemon_weight'] == "6.0 kg"
        assert merge_vars['pokemon_abilities'] == "static, lightning-rod"
        assert merge_vars['pokemon_artwork'] == "https://example.com/pikachu.png"
        
        assert call_args[1]['headers'] == {"Content-Type": "application/json"}

def test_send_pokemon_to_trmnl_missing_env(sample_pokemon_data):
    with pytest.raises(KeyError) as exc_info:
        send_pokemon_to_trmnl(sample_pokemon_data)
    assert "TRMNL_WEBHOOK_URL" in str(exc_info.value)

def test_send_pokemon_to_trmnl_api_error(sample_pokemon_data, mock_env_webhook_url):
    with patch('requests.post') as mock_post:
        mock_post.return_value = Mock(status_code=500)
        
        with pytest.raises(Exception) as exc_info:
            send_pokemon_to_trmnl(sample_pokemon_data)
        assert "Failed to send data to webhook: 500" in str(exc_info.value)

def test_send_pokemon_to_trmnl_network_error(sample_pokemon_data, mock_env_webhook_url):
    with patch('requests.post') as mock_post:
        mock_post.side_effect = requests.exceptions.RequestException("Network Error")
        
        with pytest.raises(requests.exceptions.RequestException):
            send_pokemon_to_trmnl(sample_pokemon_data)

def test_send_pokemon_to_trmnl_invalid_data():
    invalid_data = {"name": "Pikachu"}
    
    with patch('requests.post') as mock_post, \
         pytest.raises(KeyError):
        send_pokemon_to_trmnl(invalid_data)