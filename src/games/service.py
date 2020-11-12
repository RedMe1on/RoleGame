import django_filters as filters

from games.models import GamesModel


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class GamesFilter(filters.FilterSet):
    game = CharFilterInFilter(field_name='name', lookup_expr='in')

    class Meta:
        model = GamesModel
        fields = ('game',)
