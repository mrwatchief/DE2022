# content of test_sysexit.py
import pandas as pd

# content of test_class.py
import diabetes_predictor


class TestDiabetesPredictor:
    def test_predict_single_record(self):
        with open('testResources/prediction_request.json') as json_file:
            data = pd.read_json(json_file)
        dp = diabetes_predictor.DiabetesPredictor()
        status = dp.predict_single_record(data)
        assert bool(status[0]) is not None
        assert bool(status[0]) is False
