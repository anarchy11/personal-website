from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from enum import Enum

class person(str, Enum):
    kanye = "kanye west"
    john = "johntron"
    scott = "scott the woz"
    
class Book(BaseModel):
    name_book: str
    description: str | None = None
    author: str
    price: float
    class Config:
        schema_extra = {
            "book1": {
                "name_book" : "Meditations: Book of Knowledge and Philosophy Handbook",
                "description" : "Meditations is a series of personal writings by Marcus Aurelius, Roman Emperor from AD 161 to 180, recording his private notes to himself and ideas on Stoic philosophy. Marcus Aurelius wrote the 12 books of the Meditations in Koine Greek as a source for his own guidance and self-improvement.",
                "author" : "Marcus Aurelius",
                "price" : 15.00
            },
            "book2": {
                "name_book" : "#Accelerate",
                "description" : "Accelerationism is the name of a contemporary political heresy: the insistence that the only radical political response to capitalism is not to protest, disrupt, critique, or détourne it, but to accelerate and exacerbate its uprooting, alienating, decoding, abstractive tendencies.",
                "author" : "Nick Land",
                "price" : 25.99
            }
        }
    
fake_person_db = [
    { "person_id" : 0, "person_nama" : "kanye west", "job" : { "Artist", "Designer", "Rapper" } },
    { "person_id" : 1, "person_name" : "johntron", "job" : {"Youtuber", "Comedian"} },
    { "person_id" : 2, "person_name" : "scott the woz", "job" : { "Youtuber", "Gamer" } }
]


origins = [ 
    "http://localhost",
    "http://localhost:8080",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/user/me")
async def read_user():
    return { "user_id" : "the current user, its me" }

@app.get("/user/{user_id}")
async def read_other_user(user_id: str):
    return { "user_id" : user_id }

@app.get("/person/{person_id}")
async def get_person(person_id: int, response : Response):
    for p in fake_person_db:
        if p["person_id"] == person_id:
            return p
    response.status_code = 404
    return { "message" : "not found" }

@app.get("/people/")
async def read_people(skip: int = 0, limit: int = 10):
    return fake_person_db[skip : skip + limit]

@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needly : str, skip : int = 0, limit : int | None = None):
    item = { "item_id" : item_id, "needly" : needly, "skip" : skip, limit : limit }
    return item

@app.get("/book/")
async def post_book(book : Book):
    return book 

@app.post("/book/")
async def post_book(book : Book):
    return book 

@app.put("/book/{book_name}")
async def update_book(book_name: str):
    result = {"msg" : book_name}
    return result