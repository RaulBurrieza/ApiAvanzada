from pydantic import BaseModel


class userInfo(BaseModel):
    name: str
    email: str
    phoneNum: str
    password: str
    Date: str
class User(BaseModel):
    userName: str
    password: str
    
class Song(BaseModel):
    id: str
    name: str
    genre: str
    artist: str
    album: str

class Post(BaseModel):
    userName: str
    song_id: str