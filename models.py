from pydantic import BaseModel

class User(BaseModel):
    id: int
    userName: str
    password: str
    
class Song(BaseModel):
    id: str
    name: str
    genre: str
    artist: str
    album: str

class userInfo(BaseModel):
    name: str
    email: str
    phoneNum: str
    password: str

class Post(BaseModel):
    userName: str
    song_id: str