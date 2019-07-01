import pytest
from django.db.models import AutoField

from model_wrappers.errors import FieldDoesNotExist


def test_attr(a, x):
    field = a.get_field(attr='y')  # django uses `name` instead of attr as `attname`
    assert field == x


def test_name(a, x):
    field = a.get_field(name='y')
    assert field == x


def test_column(a, x):
    field = a.get_field(column='z')
    assert field == x


def test_pk(a, pk):
    field = a.get_field(name='pk')
    assert field == pk


def test_multi(a, x):
    field = a.get_field(name='y', column='z')
    assert field == x


def test_no_lookup(a):
    with pytest.raises(ValueError) as captured:
        a.get_field()
    assert str(captured.value) == 'No lookup provided'


def test_not_found(a):
    with pytest.raises(FieldDoesNotExist) as captured:
        a.get_field(name='a')
    assert captured.value.kwargs == {
        'name': 'a',
    }


def test_multi_not_found(a):
    with pytest.raises(FieldDoesNotExist) as captured:
        a.get_field(name='pk', column='z')
    assert captured.value.kwargs == {
        'name': 'pk',
        'column': 'z',
    }
