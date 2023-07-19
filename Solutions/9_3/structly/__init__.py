# structly/__init__.py

from .reader import *
from .structure import *
from .tableformat import *

__all__ = [*structure.__all__, *reader.__all__, *tableformat.__all__]
