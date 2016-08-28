# encoding: utf-8

"""
Connector (line) shape and related objects. A connector is a line shape
having end-points that can be connected to other objects (but not to other
connectors). A line can be straight, have elbows, or can be curved.
"""

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from .base import BaseShape
from ..util import Emu


class Connector(BaseShape):
    """
    Connector (line) shape. A connector is a linear shape having end-points
    that can be connected to other objects (but not to other connectors).
    A line can be straight, have elbows, or can be curved.
    """
    @property
    def begin_x(self):
        """
        Return the X-position of the begin point of this connector, in
        English Metric Units (as an |Emu| object).
        """
        cxnSp = self._element
        x, cx, flipH = cxnSp.x, cxnSp.cx, cxnSp.flipH
        begin_x = x+cx if flipH else x
        return Emu(begin_x)