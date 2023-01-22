from csv import DictReader
from django.core.management import BaseCommand

from words.models import Word


class Command(BaseCommand):
    help = "Loads data from dictionary csv file"

    def add_arguments(self, parser):
        parser.add_argument("filename", type=str, help="Name of csv file to import")

    def handle(self, *args, **kwargs):
        with open(kwargs["filename"], "r") as file:
            words = self._parse_csv_file(file)
            Word.objects.bulk_create(words)

    def _parse_csv_file(self, file):
        for row in DictReader(file):
            yield Word(
                rank=int(row["순위"]) if row["순위"] else None,
                spelling=row["단어"],
                origin=row["풀이"],
                type=row["품사"] + "사",
                word_class=row["등급"],
            )
