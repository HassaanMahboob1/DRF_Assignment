from django_filters import FilterSet
from django_filters import BooleanFilter
from django_filters import rest_framework as filters
from .models import Notes


class ArchiveFilter(filters.FilterSet):
    is_archive = filters.BooleanFilter(method="filter_is_archive")

    class Meta:
        model: Notes
        fields = ("is_archive",)

    def filter_is_archive(self, queryset, name, value):
        print("value : ", value)
