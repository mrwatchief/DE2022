from keras.models import load_model


class DiabetesPredictor:
    def __init__(self):
        self.model = None

    def predict_single_record(self, df):
        if self.model is None:
            self.model = load_model('model.h5')
        y_pred = self.model.predict(df)
        print(y_pred[0])
        status = (y_pred[0] > 0.5)
        return status
