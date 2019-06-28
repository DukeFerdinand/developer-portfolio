import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from db.models.models import Page as PageModel
from db.models.models import PageData as PageDataModel


class Page(MongoengineObjectType):

    class Meta:
        model = PageModel
        interfaces = (Node,)


class Query(graphene.ObjectType):
    node = Node.Field()
    all_pages = MongoengineConnectionField(Page)
    # role = graphene.Field(Role)


schema = graphene.Schema(query=Query)
