from model_wrappers import ModelWrapper
from ..models import A


def test_eq(a, b):
    assert a == ModelWrapper(A)
    assert a == A
    assert a != b
    assert a != 0


def test_properties(a):
    assert a.table_name == 'test00_basic_a'
