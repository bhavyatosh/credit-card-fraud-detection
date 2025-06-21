import joblib
import gdown
import os

def load_model():
    model_file = 'rf_model.pkl'

    # Download model if it doesn't exist locally
    if not os.path.exists(model_file):
        file_id = '1M335urwSbPUpW6ghyssTsPVx8WsnyVlk'
        url = f'https://drive.google.com/uc?id={file_id}'
        gdown.download(url, model_file, quiet=False)

    # Load and return the model
    model = joblib.load(model_file)
    return model
