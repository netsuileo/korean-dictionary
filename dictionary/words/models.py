import random
from django.db import models

from words.utils import nullable


class WordManager(models.Manager):
    def random(self, amount: int = 1):
        return random.sample(list(self.all()), amount)

    def search(self, word: str, limit: int):
        return self.filter(
            models.Q(spelling__contains=word) |
            models.Q(meaning__contains=word)
        ).order_by("spelling")[:limit]


class Word(models.Model):
    """A model to represent dictionary word"""

    NOUN = "명사"
    PRONOUN = "대명사"
    NUMBER = "수사"
    VERB = "동사"
    ADJECTIVE = "형용사"
    DETERMINER = "관형사"
    ADVERB = "부사"
    INTERJECTION = "감탄사"
    POST_POSITION = "조사"

    PARTS_OF_SPEECH = [
        (NOUN, "Noun"),
        (PRONOUN, "Pronoun"),
        (NUMBER, "Number"),
        (VERB, "Verb"),
        (ADJECTIVE, "Adjective"),
        (DETERMINER, "Determiner"),
        (ADVERB, "Adverb"),
        (INTERJECTION, "Interjection"),
        (POST_POSITION, "Post-position"),
    ]

    CLASS_A = "A"
    CLASS_B = "B"
    CLASS_C = "C"

    WORD_CLASSES = [
        (CLASS_A, "A"),
        (CLASS_B, "B"),
        (CLASS_C, "C"),
    ]

    rank = models.PositiveIntegerField("Frequency rank", db_index=True, **nullable)
    spelling = models.CharField("Spelling", max_length=32)
    meaning = models.CharField("Meaning", max_length=256, **nullable)

    objects = WordManager()

    @property
    def spelling_display(self):
        """Word spelling without identification numbers at the end of word"""
        digits = "0123456789"
        digits_removal = str.maketrans("", "", digits)
        return self.spelling.translate(digits_removal)

    @property
    def naver_dictionary_url(self):
        """A URL to page in Naver korean dictionary"""
        return f"https://korean.dict.naver.com/koendict/#/search?query={self.spelling_display}"

    @property
    def english_wikitionary_url(self):
        """A URL to page in English wikitionary"""
        return f"https://en.wiktionary.org/wiki/{self.spelling_display}#Korean"

    @property
    def korean_wikitionary_url(self):
        """A URL to page in Korean wikitionary"""
        return f"https://ko.wiktionary.org/wiki/{self.spelling_display}"

    def __str__(self) -> str:
        return f"{self.spelling_display}"
