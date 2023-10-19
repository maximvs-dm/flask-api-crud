from flask import Blueprint, request, current_app
from .model import Game
from .serializer import GameSchema

from pprint import pprint

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
                                    type: string
                                    description: game console
                                genre:
                                    type: string
                                    description: game genre
        """
    gs = GameSchema(many=True)
    result = Game.query.all()
    return gs.jsonify(result), 200


@bp_games.route('/adicionar', methods=['post'])
def new_game():
    """
        Add new game
        ---
        tags:
            - games
        parameters:
          - in: body
            name: body
            schema:
                id: Game2
                required:
                    - title
                    - console
                    - genre
                properties:
                    title:
                        type: string
                        description: game title
                    console:
                        type: string
                        description: game console
                    genre:
                        type: string
                        description: game genre
        responses:
            200:
                description: Game added successfully
        """
    gs = GameSchema()
    pprint(request.json)
    game = gs.load(request.json)
    current_app.db.session.add(game)
    current_app.db.session.commit()
    return 'ok', 200


                    # console:
                    #     type: array
                    #     description: list of consoles for which the game is available
                    #     items:
                    #         type: string

@bp_games.route('/excluir/<int:id>', methods=['delete'])
def delete_game(id):
    pass


@bp_games.route('/atualizar/<int:id>', methods=['put'])
def edit_game(id):
    pass
