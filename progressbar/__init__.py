from datetime import date

from .utils import streams

from .widgets import (
    Timer,
    ETA,
    AdaptiveETA,
    AbsoluteETA,
    DataSize,
    FileTransferSpeed,
    AdaptiveTransferSpeed,
    AnimatedMarker,
    Counter,
    Percentage,
    FormatLabel,
    SimpleProgress,
    Bar,
    ReverseBar,
    BouncingBar,
    RotatingMarker,
    DynamicMessage,
    FormatCustomText
)

from .bar import (
    ProgressBar,
    DataTransferBar,
    NullBar,
)
from .base import UnknownLength


from .__about__ import (
    __author__,
    __version__,
)

__date__ = str(date.today())
__all__ = [
    'streams',
    'Timer',
    'ETA',
    'AdaptiveETA',
    'AbsoluteETA',
    'DataSize',
    'FileTransferSpeed',
    'AdaptiveTransferSpeed',
    'AnimatedMarker',
    'Counter',
    'Percentage',
    'FormatLabel',
    'SimpleProgress',
    'Bar',
    'ReverseBar',
    'BouncingBar',
    'UnknownLength',
    'ProgressBar',
    'DataTransferBar',
    'RotatingMarker',
    'DynamicMessage',
    'FormatCustomText',
    'NullBar',
    '__author__',
    '__version__',
]
