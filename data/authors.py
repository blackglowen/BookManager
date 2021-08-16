from os import name
from books.models import Author
import json
from pathlib import Path

__path = Path(__file__).resolve().parent
__books = []

with open(str(__path / 'books.json')) as data:
 __books = json.load(data) 

DEFAULT_AUTHORS = [ {'name': book['author'], 'country': book['country']} for book in __books ]
