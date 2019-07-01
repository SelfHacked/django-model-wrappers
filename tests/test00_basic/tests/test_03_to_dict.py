import pytest

from model_wrappers.errors import FieldDoesNotExist
from ..models import A

obj = A(primary_key=1, y=10)
obj2 = A(primary_key=2)


def test_to_dict(a):
    assert a.to_dict(obj) == {
        'primary_key': 1,
        'y': 10,
    }


def test_to_dict_field(a):
    assert a.to_dict(obj, fields='y') == {
        'y': 10,
    }


def test_to_dict_pk(a):
    assert a.to_dict(obj, fields=['pk']) == {
        'primary_key': 1,
    }


def test_raise_unknown_field(a):
    vals = {
        'y': 10,
        'z': 5,
    }
    with pytest.raises(FieldDoesNotExist):
        a.to_dict(vals)
    assert a.to_dict(vals, raise_unknown_field=False) == {
        'y': 10,
    }


def test_keep_none(a):
    assert a.to_dict(obj2) == {
        'primary_key': 2,
        'y': None,
    }
    assert a.to_dict(obj2, keep_none=False) == {
        'primary_key': 2,
    }


def test_to_dicts(a):
    assert list(a.to_dicts([obj, obj2])) == [
        a.to_dict(obj),
        a.to_dict(obj2),
    ]
