from fastapi import FastAPI

from cassandra.cqlengine.management import sync_table

from . import config, db
from .users.models import User

DB_SESSION = None

app = FastAPI()
# settings = config.get_settings()

@app.on_event("startup")
def on_startup():
    # triggered when fastapi starts
    print("999999999999")
    global DB_SESSION
    DB_SESSION = db.get_session()
    sync_table(User)


@app.get("/")
def homepage():
    return {"hello": "homepage"}

@app.get("/users")
def users_list_view():
    q = User.objects.all().limit(10)
    return list(q)