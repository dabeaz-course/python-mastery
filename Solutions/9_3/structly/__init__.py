# structly/__init__.py

from .structure import *
from .reader import *
from .tableformat import *

__all__ = [  *structure.__all__,
            *reader.__all__,
            *tableformat.__all__ ]
