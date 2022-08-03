from django.core.management.base import BaseCommand, CommandError
from goldentravel.tours.models import Tours, TourShots


class Command(BaseCommand):
    help = 'Create a 100 new tour objects from django database'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        print("HEllo")
        obj = Tours.objects.all()
        for i in obj:
            i.delete()

        print("SUCCESS")
        # for i in range(100):
        #     print("Создание тура №:", i)
        #     Tours.objects.create(title='NewTitle', description='New description')
        # for poll_id in options['poll_ids']:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)
        #
        #     poll.opened = False
        #     poll.save()
        #
        #     self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
