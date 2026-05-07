from fastapi import FastAPI
import pandas as pd
from pathlib import Path

try:
    from .walter import Walter
except ImportError:
    from walter import Walter



app = FastAPI(title="Titanic (James)")


class James:
    def __init__(self):
        pass
    
    def get_data(self):
        w = Walter()
        return w.get_data()