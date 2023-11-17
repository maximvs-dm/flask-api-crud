from flask import Blueprint, request, current_app
from .model import Game
from .serializer import GameSchema

import ipdb

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
                            id: ReadGame
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
                id: CreateGame
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
    # pprint(request.json)
    game = gs.load(request.json)
    # print(game, type(game))
    current_app.db.session.add(game)
    current_app.db.session.commit()
    # ipdb.set_trace()
    return {
        'message': 'game created succesfully', 'data': gs.dump(game)
    }, 200


@bp_games.route('/excluir/<int:id>', methods=['delete'])
def delete_game(id):
    """
        Delete game
        ---
        tags:
            - games
        parameters:
          - in: path
            name: id
            type: int
            description: id of the game to be deleted
        responses:
            200:
                description: Game deleted successfully
            404:
                description: Game not found
        """
    query = Game.query.filter(Game.id == id)
    game = query.first()
    # ipdb.set_trace()
    if not game:
        return f'Game {id} not found', 404
    title = game.title
    query.delete()
    current_app.db.session.commit()
    return f'Game {title} deleted successfully', 200


@bp_games.route('/atualizar/<int:id>', methods=['put'])
def edit_game(id):
    """
        Update game
        ---
        tags:
            - games
        parameters:
          - in: path
            name: id
            type: int
            description: id of the game to be deleted

          - in: body
            name: body
            schema:
                id: CreateGame
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
                description: Game updated successfully
            404:
                description: Game not found
        """
    gs = GameSchema()
    query = Game.query.filter(Game.id == id)
    game = query.first()
    if not game:
        return f'Game {id} not found', 404
    query.update(request.json)
    current_app.db.session.commit()
    # ipdb.set_trace()
    return {
        'message': f'Game {game.title} updated successfully',
        'data': gs.dump(game)
    }, 200
