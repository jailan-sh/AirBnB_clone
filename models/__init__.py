#!/usr/bin/python3

""" module to call/create database storage of app"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
