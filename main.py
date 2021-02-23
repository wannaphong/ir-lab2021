from fastapi import FastAPI
from pythainlp.tokenize import word_tokenize

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/word_tokenize/{text}")
def read_word(text: str):
    return {"word": word_tokenize(text)}