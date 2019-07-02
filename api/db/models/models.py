from datetime import datetime
from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import DateTimeField, StringField, EmbeddedDocumentField


class PageSection(Document):
    meta = {'collection': 'page_section'}


class PageData(EmbeddedDocument):
    '''
    CMS Page content, assorted options will vary based on page you're constructing

    Attributes
    ----------
    page_title: string
        Title to be supplied to the page <head>
    '''
    page_title = StringField(required=True)
    page_body = StringField()


class Page(Document):
    '''
    The base CMS page.

    Attributes
    ----------
    page_type: string
        The page type, like ``front_page`` or ``contact_me``
    page_data: PageData
        PageData embedded document
    updated_on: datetime
        Gets set automatically by default,
        update manually with something like ``datetime.now()``
    '''
    meta = {'collection': 'page_class'}
    page_type = StringField(required=True, unique=True)
    page_data = EmbeddedDocumentField(PageData, required=True)
    updated_on: DateTimeField(default=datetime.now)
