import joblib

def predict(data):
    model = joblib.load('rf_model.sav')
    return model.predict(data)
