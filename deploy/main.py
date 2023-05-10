import uvicorn
import tensorflow as tf

from typing import Union
from fastapi import FastAPI

def predict(gambar):
    loaded_model = tf.keras.models.load_model('handsign_model_v1.h5')
    gambar = tf.expand_dims(gambar, 0)
    return tf.argmax(loaded_model(gambar)[0])


app = FastAPI()

@app.get("/")
def read_root():
    dummy_input = tf.random.uniform((28,28,1))
    hasil = predict(dummy_input)
    print(hasil)
    return int(hasil.numpy())

uvicorn.run(app, host='0.0.0.0',port=8001)