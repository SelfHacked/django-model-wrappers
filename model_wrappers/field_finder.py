from returns import (
    returns as _returns,
)

from .errors import (
    FieldDoesNotExist as _FieldDoesNotExist,
)
from .util import cached_property
from .util.datatypes import (
    ImmutableDict as _ImmutableDict,
)


class AbstractModelFieldFinder(object):
    def __init__(self, model: 'ModelWrapper'):
        self.__model = model

    @property
    def model(self) -> 'ModelWrapper':
        return self.__model

    def __getitem__(self, val) -> 'FieldWrapper':
        raise NotImplementedError  # pragma: no cover


class ModelFieldFinders(object):
    def __init__(self, **finders: AbstractModelFieldFinder):
        self.__finders = finders

    def __getitem__(self, name) -> AbstractModelFieldFinder:
        return self.__finders[name]

    def get(self, **kwargs) -> 'FieldWrapper':
        result = None

        for name, val in kwargs.items():
            if val is None:
                continue

            if result is None:
                result = self[name][val]
                continue

            if result == self[name][val]:
                continue

            raise _FieldDoesNotExist(**kwargs)

        if result is None:
            raise ValueError('No lookup provided')
        return result


class AttributeModelFieldFinder(AbstractModelFieldFinder):
    def __init__(self, model: 'ModelWrapper', attr: str):
        super().__init__(model)
        self.__attr = attr

    @property
    def attr(self) -> str:
        return self.__attr

    @cached_property
    @_returns(_ImmutableDict)
    def _cache(self) -> _ImmutableDict:
        for field in self.model.fields:
            yield getattr(field, self.attr), field

    def __getitem__(self, val) -> 'FieldWrapper':
        try:
            return self._cache[val]
        except KeyError:
            raise _FieldDoesNotExist(**{self.attr: val})


class NameModelFieldFinder(AttributeModelFieldFinder):
    def __init__(self, model: 'ModelWrapper'):
        super().__init__(model, 'name')

    def __getitem__(self, val: str) -> 'FieldWrapper':
        if val == 'pk':
            return self.model.pk
        return super().__getitem__(val)


from .field import FieldWrapper
from .model import ModelWrapper
