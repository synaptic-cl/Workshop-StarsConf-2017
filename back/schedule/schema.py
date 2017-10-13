import graphene
from graphene_django import DjangoObjectType

from schedule import models


class Talk(DjangoObjectType):
    class Meta:
        model = models.Talk


class TimeSlot(DjangoObjectType):
    class Meta:
        model = models.TimeSlot


class Speaker(DjangoObjectType):
    class Meta:
        model = models.Speaker


class Query(graphene.ObjectType):
    all_talks = graphene.List(Talk)
    all_time_slots = graphene.List(TimeSlot)
    all_speakers = graphene.List(Speaker)
    talk = graphene.Field(Talk, id=graphene.Int(required=True))
    time_slot = graphene.Field(TimeSlot, id=graphene.Int(required=True))
    speaker = graphene.Field(Speaker, id=graphene.Int(required=True))

    @graphene.resolve_only_args
    def resolve_all_talks(self):
        return models.Talk.objects.all()

    @graphene.resolve_only_args
    def resolve_all_time_slots(self):
        return models.TimeSlot.objects.all()

    @graphene.resolve_only_args
    def resolve_all_speakers(self):
        return models.Speaker.objects.all()

    @graphene.resolve_only_args
    def resolve_talk(self, id):
        # this returns None if no row is found
        return models.Talk.objects.filter(pk=id).first()

    @graphene.resolve_only_args
    def resolve_time_slot(self, id):
        return models.TimeSlot.objects.filter(pk=id).first()

    @graphene.resolve_only_args
    def resolve_speaker(self, id):
        return models.Speaker.objects.filter(pk=id).first()


schema = graphene.Schema(query=Query)
