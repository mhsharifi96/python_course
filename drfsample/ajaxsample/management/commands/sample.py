from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        # parser.add_argument('number', type=int)
        parser.add_argument(
            '--delete',
            action='store_true',
            help='Delete poll instead of closing it',
        )


    def handle(self, *args, **options):
        print(options)
        print('run simple custom command')
        # for poll_id in options['poll_ids']:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)

        #     poll.opened = False
        #     poll.save()

        self.stdout.write(self.style.SUCCESS('Successfully closed "%s"' %options['number']))