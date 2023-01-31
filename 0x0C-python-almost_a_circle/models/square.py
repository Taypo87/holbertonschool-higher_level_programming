#!/usr/bin/python3
"""Class square inherits from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represnts a square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
