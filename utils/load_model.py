#global load_model
from keras.models import load_model
def init():
    return load_model("./sentimentLSTM.h5")