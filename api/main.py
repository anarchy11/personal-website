from fastapi import FastAPI
from enum import Enum

class person(str, Enum):
    kanye = "kanye west"
    john = "johntron"
    scott = "scott the woz"
    
fake_person_db = [
    { "person_nama" : "kanye west", "job" : { "Artist", "Designer", "Rapper" } },
    { "person_name" : "johntron", "job" : {"Youtuber", "Comedian"} },
    { "person_name" : "scott the woz", "job" : { "Youtuber", "Gamer" } }
]

app = FastAPI()

@app.get("/user/me")
async def read_user():
    return { "user_id" : "the current user, its me" }

@app.get("/user/{user_id}")
async def read_other_user(user_id: str):
    return { "user_id" : user_id }

@app.get("/people/")
async def read_people(skip: int = 0, limit: int = 10):
    return fake_person_db[skip : skip + limit]

@app.get("/person/{person_name}")
async def get_person(person_name: person):
    if person_name == person.kanye:
        return { "person_nama" : person_name, "job" : { "Artist", "Designer", "Rapper" } }
    
    if person_name == person.john:
        return { "person_name" : person_name, "job" : {"Youtuber", "Comedian"} }
    
    return { "person_name" : person_name, "job" : { "Youtuber", "Gamer" } }