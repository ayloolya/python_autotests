import requests

response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons',
                        json={
                            "name": "Кит",
                            "photo": "https://dolnikov.ru/pokemons/albums/053.png"
                            },
                        headers={
                            'trainer_token':'f02c48bb71caf77c61e743460deaf3e7',
                            'Content-Type': 'application/json'
                            }
                        )
print(response.text)

response = requests.put(url='https://api.pokemonbattle.me:9104/pokemons',
                        json={
                            "pokemon_id": "20773",
                            "name": "Утконос",
                            "photo": "https://dolnikov.ru/pokemons/albums/054.png"
                            },
                        headers={
                            'trainer_token':'f02c48bb71caf77c61e743460deaf3e7',
                            'Content-Type': 'application/json'
                            }
                        )
print(response.text)

response = requests.post(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball',
                        json={
                            "pokemon_id": "20773",
                            },
                        headers={
                            'trainer_token':'f02c48bb71caf77c61e743460deaf3e7',
                            'Content-Type': 'application/json'
                            }
                        )
print(response.text)