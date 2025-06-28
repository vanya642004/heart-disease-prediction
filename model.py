import pickle
import os

def predict_from_inputs(input_data):
    model_path = "model.pkl"
    if not os.path.exists(model_path):
        raise FileNotFoundError("Model file not found. Train the model and upload model.pkl.")

    with open(model_path, "rb") as f:
        model = pickle.load(f)

    prediction = model.predict([input_data])
    return prediction[0]
