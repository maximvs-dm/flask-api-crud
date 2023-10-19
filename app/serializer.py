from flask_marshmallow import Marshmallow

from .model import Game

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class GameSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Game
