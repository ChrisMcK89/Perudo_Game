import requests

# Test creating number of players
url = 'http://127.0.0.1:5000/numberofplayers'
data = {
    'number_of_players': 4
}
response = requests.post(url, json=data)
assert response.status_code == 201
assert response.json()['message'] == 'Player count 4 created successfully.'

# Test creating player
url = 'http://127.0.0.1:5000/players'
data = {
    'name': 'Alice',
    'colour': 'red'
}
response = requests.post(url, json=data)
assert response.status_code == 201
assert response.json()['message'] == 'Player Alice created successfully.'

# Test getting players
url = 'http://127.0.0.1:5000/players'
response = requests.get(url)
assert response.status_code == 200
assert len(response.json()) == 1
assert response.json()[0]['name'] == 'Alice'
assert response.json()[0]['colour'] == 'red'
print(response.json()[0]['name'])