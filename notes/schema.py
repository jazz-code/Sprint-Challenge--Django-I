from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from .models import Note
from .models import PersonalNote

# what type of data is going to make up our nodes?
# each note in our DB will act as node in our GraphQL endpoint

# we are telling graphene what we want to export
# inherits from DjangoObjectType
class NoteType(DjangoObjectType):
    # nested Class
    class Meta:
        # models to export
        model = Note
        # we tell it what type of data this is, i.e is it in relation between this data and other data or a node itself
        # this is a node (tuple,)
        interfaces = (graphene.relay.Node,)

class PersonalNoteType(DjangoObjectType):
    class Meta:
        model = PersonalNote
        interfaces = (graphene.relay.Node,)
#when we query, which records do we return?
class Query(graphene.ObjectType):
    # when we do a query on notes, return a List (of objects that correspond to NoteType (and NoteType corresponds to Note model))
    notes = graphene.List(NoteType)
    personalnotes = graphene.List(PersonalNoteType)
    # override method
    def resolve_notes(self, info):
        # return a list of notes, all notes
        return Note.objects.all()

    def resolve_personalnotes(self, info):
        return PersonalNote.objects.all()
# expose this query to graphene
schema = graphene.Schema(query=Query)
