from csv import DictReader
from django.core.management import BaseCommand

from words.models import Word


class Command(BaseCommand):
    help = "Removes duplicate words from database"

    def handle(self, *args, **kwargs):
        self._remove_numbers_at_the_end_of_words()
        self._remove_duplicate_words()

    def _remove_numbers_at_the_end_of_words(self):
        for word in Word.objects.all():
            word.spelling = word.spelling_display
            word.save()

    def _remove_duplicate_words(self):
        ids_to_exclude = []
        for word in Word.objects.order_by("rank").all():
            if word.rank and word.rank % 100 == 0:
                print(f"Current word id: {word.id}")
            ids_to_exclude.append(word.id)
            duplicates = Word.objects.filter(spelling=word.spelling).exclude(
                pk__in=ids_to_exclude
            )

            for duplicate in duplicates:
                ids_to_exclude.append(duplicate.id)
                duplicate.delete()
