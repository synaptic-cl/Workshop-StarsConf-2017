import os
import csv
from django.core.management.base import BaseCommand
from schedule.models import Talk, Speaker, TimeSlot

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Command(BaseCommand):
    help = 'Populate the talks of the conference'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Done'))
        with open(os.path.join(BASE_DIR, 'talks.csv')) as csvfile:
            reader = csv.DictReader(csvfile, delimiter='|')

            for pos, row in enumerate(reader):
                talk = Talk(id=pos + 1, name=row['name'],
                            category=row['category'] or '')
                if row['room']:
                    talk.room = row['room']
                else:
                    talk.room = '-'

                timeslots = TimeSlot.objects \
                                    .filter(date=row['date'], start=row['start']) \
                                    .order_by('end')
                if talk.room == 'colorada':
                    talk.time_slot = timeslots[1]
                else:
                    talk.time_slot = timeslots[0]

                if row['speaker']:
                    speaker, created = Speaker.objects.get_or_create(name=row['speaker'])
                    talk.speaker = speaker
                # self.stdout.write(str(row))

                talk.is_placeholder = not talk.speaker
                talk.save()
                self.stdout.write(str(talk))
        self.stdout.write(self.style.SUCCESS('Done'))
