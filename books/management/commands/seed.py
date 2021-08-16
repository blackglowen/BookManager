from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from faker import Faker
from books import models
from data import genres, authors

def create_authors():
    for author in authors.DEFAULT_AUTHORS:
        auth = models.Author(name=author['name'], country=author['country'])
        auth.save()
        

def create_genres():
    for genre in genres.DEFAULT_CATEGORIES:
        cat = models.Category(name=genre)
        cat.save()

def create_user():
    faker = Faker()
    first_name = faker.first_name()
    last_name = faker.last_name()
    email = '{}.{}@example.com'.format(first_name.lower(), last_name.lower())
    password = 'Pwd987654321@'
    username = first_name.lower() + '.' + last_name.lower()
    user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
    user.save()

class Command(BaseCommand):
    help = 'Populates the database with records'
    
    def add_arguments(self, parser):
        self.parser = parser
        parser.add_argument('-u', '--users', metavar='N', type=int, help='The number of fake users to create.')
        parser.add_argument('-g', '--genres', action='store_true', help='Flag to create default book genres.')
        parser.add_argument('-a', '--authors', action='store_true', help='Flag to create default authors.')
                   
    def handle(self, *args, **options):
        if options['users']:
            for _ in range(options['users']):
                create_user()
            self.stdout.write(self.style.SUCCESS('Successfully created %s users' % options['users']))
            
        if options['genres']:
            create_genres()
            self.stdout.write(self.style.SUCCESS('Successfully created book genres'))
        
        if options['authors']:
            create_authors()
            self.stdout.write(self.style.SUCCESS('Successfully created book authors'))

        if not (options['users'] or options['genres'] or options['authors']):
            self.parser.print_help()