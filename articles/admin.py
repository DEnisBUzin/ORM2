from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            # form.cleaned_data
            if form.cleaned_data.get('is_main'):
                count += 1
                if count > 1:
                    raise ValidationError("Здесь должен быть единственный главный тэг")

        if count == 0:
            raise ValidationError("У каждой новости должен быть хотя бы один основной тэг")
        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]

admin.site.register(Scope)
admin.site.register(Tag)