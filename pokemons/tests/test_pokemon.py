import requests
import pytest

def test_status_code():
    response = requests.get(url='https://api.pokemonbattle.me:9104/trainers')
    assert response.status_code == 200

def test_trainer_name():
    response = requests.get(url='https://api.pokemonbattle.me:9104/trainers', params={'trainer_id' : 3565})
    assert response.json()['trainer_name'] == 'Оля', ''