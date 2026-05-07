from fastapi import FastAPI
import pandas as pd
from pathlib import Path

try:
    from .doro_reader import DoroReader
except ImportError:
    from doro_reader import DoroReader



app = FastAPI(title="Doro Data")


class DoroDirector:
    def __init__(self):
        pass
    
    def get_data(self):
        dr = DoroReader()
        return dr.get_data()