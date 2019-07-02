import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from db.models.models import Page as PageModel
from db.models.models import PageData as PageDataModel


class CMSPage(MongoengineObjectType):

    class Meta:
        model = PageModel
        interfaces = (Node,)


class Query(graphene.ObjectType):
    node = Node.Field()
    all_cms_pages = MongoengineConnectionField(CMSPage)
    cms_page = graphene.Field(CMSPage, page_type=graphene.String())
    # role = graphene.Field(Role)


schema = graphene.Schema(query=Query)
