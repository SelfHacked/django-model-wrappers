from model_wrappers import FieldWrapper
from ..models import A


def test_eq(x, pk, pk2):
    raw = A._meta.get_field('y')
    assert x == FieldWrapper(raw)
    assert x == raw
    assert x != pk
    assert x != pk2
    assert x != 0


def test_properties(x):
    assert x.attr == 'y'  # django uses `name` instead of attr as `attname`
    assert x.name == 'y'
    assert x.column == 'z'
