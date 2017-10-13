from django.contrib import admin
from easy_select2 import select2_modelform

from .models import TimeSlot, Talk, Speaker

TalkForm = select2_modelform(Talk, attrs={'width': '250px'})


class TalkAdmin(admin.ModelAdmin):
    list_display = ('name', 'time_slot', 'speaker', 'room', 'category', 'is_placeholder')
    form = TalkForm


class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'n_talks')

    def n_talks(self, obj):
        return obj.talk_set.count()
    n_talks.short_description = 'Number of talks'


class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'n_talks')

    def n_talks(self, obj):
        return obj.talk_set.count()
    n_talks.short_description = 'Number of talks'


admin.site.register(TimeSlot, TimeSlotAdmin)
admin.site.register(Talk, TalkAdmin)
admin.site.register(Speaker, SpeakerAdmin)
