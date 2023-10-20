from flask_marshmallow import Marshmallow
from marshmallow import post_load

from .model import Game

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class GameSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Game

    @post_load
    def make_game(self, data, **kwargs):
        return Game(**data)
