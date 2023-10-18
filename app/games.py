from flask import Blueprint

bp_games = Blueprint('games', __name__)


@bp_games.route('/exibir')
def show_games():
    pass


@bp_games.route('/adicionar', methods=['post'])
def new_game():
    pass


@bp_games.route('/excluir/<int:id>', methods=['delete'])
def delete_game(id):
    pass


@bp_games.route('/atualizar/<int:id>', methods=['put'])
def edit_game(id):
    pass
