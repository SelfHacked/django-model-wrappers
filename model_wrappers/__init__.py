__version__ = '0.1dev0'

try:
    from .field import FieldWrapper
    from .model import ModelWrapper
except ImportError:  # pragma: nocover
    pass
