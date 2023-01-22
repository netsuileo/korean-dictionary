from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Word


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = [
        "rank",
        "spelling",
        "meaning",
        "naver_dictionary_url",
        "english_wikitionary_url",
        "korean_wikitionary_url",
    ]
    search_fields = ["spelling", "origin"]

    def naver_dictionary_url(self, instance):
        return self._create_link(instance.naver_dictionary_url, "Naver")

    def english_wikitionary_url(self, instance):
        return self._create_link(instance.english_wikitionary_url, "EN Wiki")

    def korean_wikitionary_url(self, instance):
        return self._create_link(instance.korean_wikitionary_url, "KO Wiki")

    def _create_link(self, url, name):
        return mark_safe(f'<a href="{url}" target="_blank" rel="nofollow">{name}</a>')
