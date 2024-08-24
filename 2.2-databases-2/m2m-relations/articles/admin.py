from pprint import pprint

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_sections = sum(
            form.cleaned_data.get('is_main', 0) for form in self.forms
        )
        print(main_sections)
        if not main_sections:
            raise ValidationError('Укажите основной раздел!')
        elif main_sections > 1:
            raise ValidationError('Основной раздел должен быть только один!')
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]

