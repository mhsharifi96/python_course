from django.core.management.base import BaseCommand, CommandError
from pprint import pprint
class Command(BaseCommand):
    help = 'python manage.py maktab --help'

    def add_arguments(self, parser):
        parser.add_argument('number', type=int)
        parser.add_argument('number1', type=int)
        parser.add_argument('number2', type=int)
        parser.add_argument('number3', type=int)

    def handle(self, *args, **options):
        pprint(options)
        print('maktab command workd :)')
        
        # for poll_id in options['poll_ids']:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)

        #     poll.opened = False
        #     poll.save()

        #     self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
        self.stdout.write(self.style.SUCCESS('Successfully closed "%s"' %options['number']))
