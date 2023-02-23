from flask_cors import CORS
from flask import Flask, request, jsonify
from player import Player


app = Flask(__name__)
CORS(app)
num_of_players = 0
players = []

@app.route('/numberofplayers', methods=['POST'])
def create_number_of_players():
    global num_of_players
    number_of_players = request.json.get('number_of_players')
    if number_of_players is not None:
        num_of_players = number_of_players
        return jsonify({'message': f'Player count {num_of_players} created successfully.'}), 201
    else:
        return jsonify({'message': 'Invalid input.'}), 400

@app.route('/players', methods=['POST'])
def create_player():
    global players, num_of_players
    name = request.json.get('name')
    colour = request.json.get('colour')
    if name and colour:
        if len(players) >= num_of_players:
            return jsonify({'message': 'Maximum number of players reached.'}), 400
        player = {
            'name': name,
            'colour': colour
        }
        players.append(player)
        return jsonify({'message': f'Player {name} created successfully.'}), 201
    else:
        return jsonify({'message': 'Invalid input.'}), 400

@app.route('/players', methods=['GET'])
def get_players():
    global players
    return jsonify(players)

if __name__ == '__main__':
    app.run(debug=True)
