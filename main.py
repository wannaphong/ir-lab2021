from fastapi import FastAPI, File, UploadFile
from pythainlp.tokenize import word_tokenize
import io
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/word_tokenize/{text}")
def read_word(text: str):
    return {"word": word_tokenize(text)}

class ImageType(BaseModel):
    url: str@app.post("/predict/") 
def prediction(request: Request, file: bytes = File(…)):
    if request.method == "POST":
        image_stream = io.BytesIO(file)
        image_stream.seek(0)
        #file_bytes = np.asarray(bytearray(image_stream.read()), dtype=np.uint8)
        #frame = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        #label = read_img(frame)
        return 'ok'#label
    return "No post request found"