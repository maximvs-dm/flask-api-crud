from flask import Blueprint

bp_games = Blueprint('games', __name__)


@bp_games.route('/exibir')
def show_games():
    """
        Create a new user
        ---
        tags:
          - users
        definitions:
          - schema:
              id: Group
              properties:
                name:
                 type: string
                 description: the group's name
        parameters:
          - in: body
            name: body
            schema:
              id: User
              required:
                - email
                - name
              properties:
                email:
                  type: string
                  description: email for user
                name:
                  type: string
                  description: name for user
                address:
                  description: address for user
                  schema:
                    id: Address
                    properties:
                      street:
                        type: string
                      state:
                        type: string
                      country:
                        type: string
                      postalcode:
                        type: string
                groups:
                  type: array
                  description: list of groups
                  items:
                    $ref: "#/definitions/Group"
        responses:
          201:
            description: User created
        """
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
