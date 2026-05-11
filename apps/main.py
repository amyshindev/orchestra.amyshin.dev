import sys
from pathlib import Path

_APPS_DIR = Path(__file__).resolve().parent
if str(_APPS_DIR) not in sys.path:
    sys.path.insert(0, str(_APPS_DIR))

from fastapi import FastAPI

try:
    from titanic.app.james_controller import JamesController
except ModuleNotFoundError:
    from apps.titanic.app.james_controller import JamesController

try:
    from doro.app.doro_director import DoroDirector
except ModuleNotFoundError:
    from apps.doro.app.doro_director import DoroDirector

app = FastAPI(title="Amy Shin Main Page")

@app.get("/")
def read_root():
    return {"message": "FAST API 메인 페이지 ", "docs": "/docs"}

@app.get("/titanic/data")
def read_titanic_data():
    james = JamesController()
    df = james.get_data()

    return df.to_dict(orient="records")


@app.get("/titanic/count")
def read_titanic_count(): 
    james = JamesController()
    count = james.get_count()

    return {"count": count}


@app.get("/titanic/count/survived")
def read_titanic_count_survived():
    james = JamesController()
    count_survived = james.get_count_survived()

    return {"count_survived": count_survived}


@app.get("/titanic/count/dead")
def read_titanic_count_dead():
    james = JamesController()
    count_dead = james.get_count_dead()

    return {"count_dead": count_dead}


@app.get("/titanic/model/name")
def read_titanic_model_name():
    james = JamesController()
    model_name = james.get_training_model_name()
    return {"model_name": model_name}


@app.get("/doro/data")
def read_doro_data():
    dorodirector = DoroDirector()
    df = dorodirector.get_data()

    return df.to_dict(orient="records")


if __name__ == "__main__":
    import uvicorn


    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)