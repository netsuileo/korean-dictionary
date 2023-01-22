from django.shortcuts import get_object_or_404, render
from django.conf import settings

from .models import Word


def index(request):
    return render(
        request,
        "words/index.html",
        context={
            "title": settings.WEBSITE_TITLE,
            "words": Word.objects.random(settings.INDEX_PAGE_RANDOM_WORDS_AMOUNT),
        },
    )


def word(request, word_id):
    word = get_object_or_404(Word, pk=word_id)
    return render(
        request,
        "words/word.html",
        context={
            "title": f"{settings.WEBSITE_TITLE}: {word.spelling}",
            "word": word,
        },
    )


def about(request):
    return render(
        request,
        "words/about.html",
        context={"title": f"{settings.WEBSITE_TITLE}: about"},
    )


def search(request, word: str):
    return render(
        request,
        "words/includes/table.html",
        context={"words": Word.objects.search(word, settings.WORD_SEARCH_SIZE_LIMIT)},
    )


def random(request):
    return render(
        request,
        "words/includes/table.html",
        context={"words": Word.objects.random(settings.INDEX_PAGE_RANDOM_WORDS_AMOUNT)},
    )
