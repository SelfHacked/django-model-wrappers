import typing as _typing

from model_wrappers.typing import (
    KT as _KT,
    VT_co as _VT_co,
)
from . import cached_property


class ImmutableDict(_typing.Mapping[_KT, _VT_co]):
    DICT_TYPE = dict

    def __init__(self, *args, **kwargs):
        self.__dict = self.DICT_TYPE(*args, **kwargs)

    @cached_property
    def _repr(self):
        return repr(self.__dict)

    def __repr__(self):
        return self._repr

    @cached_property
    def _str(self):
        return str(self.__dict)

    def __str__(self):
        return self._str

    @cached_property
    def _items(self):
        return self.__dict.items()

    def items(self):
        return self._items

    @cached_property
    def _keys(self):
        return self.__dict.keys()

    def keys(self):
        return self._keys

    @cached_property
    def _values(self):
        return self.__dict.values()

    def values(self):
        return self._values

    @cached_property
    def _len(self):
        return len(self.__dict)

    def __len__(self) -> int:
        return self._len

    @cached_property
    def _hash(self):
        return hash(tuple(self._items))

    def __hash__(self):
        return self._hash

    def __contains__(self, k: _KT):
        return k in self.__dict

    def __getitem__(self, k: _KT) -> _VT_co:
        return self.__dict[k]

    def get(self, k: _KT) -> _typing.Optional[_VT_co]:
        return self.__dict.get(k)

    def __iter__(self) -> _typing.Iterator:
        return iter(self.__dict)
