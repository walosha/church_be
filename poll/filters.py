from django.db.models import Q, Count
from django_filters import rest_framework as df_filters
from django.utils import timezone
from core.fields import MultipleFilter, DateRangeFilter
from .models import Poll


class PollFilter(df_filters.FilterSet):
    status = MultipleFilter(field_name='status')
    name = df_filters.CharFilter(field_name="name", lookup_expr="icontains")
    type = MultipleFilter(field_name='type')
    start_date = DateRangeFilter(field_name='start_date')
    search = df_filters.CharFilter(field_name="name", lookup_expr='icontains')
    non_draft = df_filters.BooleanFilter(method="filter_non_draft")

    class Meta:
        model = Poll
        fields = ['type', 'start_date', 'name']

    @staticmethod
    def filter_non_draft(queryset, name, value):
        if value:
            return queryset.exclude(status='DRAFT')
        return queryset
