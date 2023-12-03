from rest_framework.filters import BaseFilterBackend
import coreapi


class PCsLaptopFilterBackend(BaseFilterBackend):
    def get_schema_fields(self, view):
        fields = [coreapi.Field(
            name='user_1',
            location='query',
            required=True,
            type='int'
        ),
            coreapi.Field(
                name='user_2',
                location='query',
                required=True,
                type='int'
        ),
        ]
        return fields

    def filter_queryset(self, request, queryset, view):
        return queryset
