import pytest

from model_wrappers.util.datatypes import ImmutableDict

d = {
    'a': 0,
    'b': 'x',
}
im = ImmutableDict(d)


def test_str():
    assert repr(im) == repr(d)
    assert str(im) == str(d)


def test_items():
    assert set(im.keys()) == {'a', 'b'}
    assert set(im.values()) == {0, 'x'}
    assert set(im.items()) == {('a', 0), ('b', 'x')}
    assert set(im) == {'a', 'b'}


def test_collection():
    assert len(im) == 2
    assert 'a' in im
    assert 'c' not in im


def test_dict():
    assert im['a'] == 0
    assert im.get('a') == 0
    with pytest.raises(KeyError):
        im['c']
    assert im.get('c') is None


def test_hashable():
    with pytest.raises(TypeError):
        {d: 0}
    {im: 0}
