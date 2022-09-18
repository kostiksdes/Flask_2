from api import ma
from api.models.author import AuthorModel


class AuthorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AuthorModel
        #fields = ("name",) #только нужные поля
        #exlude = ("id", )


author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)
