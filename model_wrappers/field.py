import django.db.models as _models
from django.db.models.expressions import (
    Col as _Col,
)

from .util import cached_property


class FieldWrapper(object):
    def __init__(
            self,
            field: _models.Field,
            *,
            model: 'ModelWrapper' = None,
    ):
        self.__raw = field
        if model is None:
            model = ModelWrapper(field.model)
        self.__model = model

    def __eq__(self, other):
        if isinstance(other, FieldWrapper):
            return self == other.raw
        if not isinstance(other, _models.Field):
            return False

        raw = self.raw
        if raw == other:
            return True

        if self.model != other.model:
            return False
        if raw.name != other.name:
            return False

        return True

    @property
    def raw(self) -> _models.Field:
        return self.__raw

    @property
    def model(self) -> 'ModelWrapper':
        return self.__model

    @property
    def column(self) -> str:
        return self.raw.column

    @property
    def attr(self) -> str:
        return self.raw.attname

    @property
    def name(self) -> str:
        return self.raw.name

    @cached_property
    def is_fk(self) -> bool:
        return isinstance(self.raw, _models.ForeignKey)

    def col(self, alias=None) -> _Col:
        alias = alias or self.model.table_name
        return self.raw.get_col(alias)


from .model import ModelWrapper
