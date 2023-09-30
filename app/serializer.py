from flask_marshmallow import Marshmallow

from .model import Jogo

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class JogoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Jogo
