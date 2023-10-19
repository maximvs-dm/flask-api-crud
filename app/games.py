from flask import Blueprint, jsonify
from flask_restful import Resource, Api, fields, marshal_with
from .model import Game
from .serializer import GameSchema

bp_games = Blueprint('games', __name__)


@bp_games.route('/exibir')
# @marshal_with(GameSchema)
def show_games():
    """
        List all games
        ---
        tags:
            - games
        responses:
            200:
                description: List of games
                schema:
                    type: array
                    items:
                        schema:
                            id: Game
                            properties:
                                id:
                                    type: number
                                    description: game id
                                title:
                                    type: string
                                    description: game title
                                console:
                                    type: array
                                    description: list of consoles for which the game is available
                                    items:
                                        type: string
                                genre:
                                    type: string
                                    description: game genre
        """
    games = [
        Game(title="Zelda BOTW", console="Switch", genre="Adventure"),
        Game(title="Zelda TOTK", console="Switch", genre="Adventure")
    ]
    return jsonify(GameSchema().dump(games, many=True))


@bp_games.route('/adicionar', methods=['post'])
def new_game():
    """
        Add new game
        ---
        tags:
            - games
        responses:
            200:
                description: Game added successfully
        """
    pass


@bp_games.route('/excluir/<int:id>', methods=['delete'])
def delete_game(id):
    pass


@bp_games.route('/atualizar/<int:id>', methods=['put'])
def edit_game(id):
    pass
