#!/usr/bin/python3
from models.engine import file_storage

storage = engine.file_storage.FileStorage(__file_path='file.json')
storage.reload()
