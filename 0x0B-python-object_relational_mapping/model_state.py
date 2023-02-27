#!/usr/bin/python3
""" Module for state class and base instance"""


from sqalchemy import Column, Integer, String
from sqalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class:
        Inhereits from Base"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
