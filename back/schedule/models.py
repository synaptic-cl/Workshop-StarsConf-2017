from django.db import models

ROOM_CHOICES = (
    ('', '-----------'),
    ('-', '-'),
    ('fresno', 'Sala Fresno'),
    ('magna', 'Sala Magna'),
    ('matte', 'Sala Matte'),
    ('talleres', 'Sala Talleres'),
)


class TimeSlot(models.Model):
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()

    def __str__(self):
        return "%s - %s-%s" % (self.date.strftime("%A %d"), self.start.strftime('%H:%M'),
                               self.end.strftime('%H:%M'))

    class Meta:
        ordering = ['date', 'start', 'end']


class Speaker(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Talk(models.Model):
    name = models.CharField(max_length=200)
    time_slot = models.ForeignKey(TimeSlot)
    speaker = models.ForeignKey(Speaker, blank=True, null=True)
    room = models.CharField(max_length=20, blank=True, choices=ROOM_CHOICES)
    category = models.CharField(max_length=100, blank=True)
    is_placeholder = models.BooleanField(default=False,
                                         help_text="True for lunch, break time, etc.")

    class Meta:
        ordering = ['id']

    def __str__(self):
        return "%s - %s - %s" % (self.time_slot, self.name, self.speaker)
