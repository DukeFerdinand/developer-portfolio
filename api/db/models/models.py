from datetime import datetime
from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import DateTimeField, StringField, EmbeddedDocumentField


class PageSection(Document):
    meta = {'collection': 'page_section'}


class PageData(EmbeddedDocument):
    page_title = StringField(required=True)


class Page(Document):
    meta = {'collection': 'page_class'}
    page_type = StringField(required=True, unique=True)
    page_data = EmbeddedDocumentField(PageData, required=True)
    updated_on: DateTimeField(default=datetime.now)
