from concurrent.futures import ThreadPoolExecutor

from django.core.management import BaseCommand
from wiktionaryparser import WiktionaryParser
from words.models import Word


class Command(BaseCommand):
    help = "Get words meaning from wikitionary"

    def handle(self, *args, **kwargs):
        words = Word.objects.filter(rank__gte=31).order_by('rank')
        with ThreadPoolExecutor(max_workers=8) as executor:
            executor.map(self._get_meaning_from_wikitionary, words)
    
    def _get_meaning_from_wikitionary(self, word):
        parser = WiktionaryParser()
        parser.set_default_language('korean')
        response = parser.fetch(word.spelling)
        try:
            translation = response[0]['definitions'][0]['text'][1]
        except (IndexError, KeyError):
            translation = None
        word.meaning = translation
        word.save()
