import pytest

from model_wrappers import ModelWrapper, FieldWrapper
from ..models import A, B


@pytest.fixture
def a():
    return ModelWrapper(A)


@pytest.fixture
def b():
    return ModelWrapper(B)


@pytest.fixture
def x():
    return FieldWrapper(A._meta.get_field('y'))


@pytest.fixture
def pk():
    return FieldWrapper(A._meta.get_field('primary_key'))


@pytest.fixture
def pk2():
    return FieldWrapper(B._meta.get_field('id'))
