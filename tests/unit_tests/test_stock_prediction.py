import unittest
import joblib
from stock_prediction import predict_price

class TestStockPrediction(unittest.TestCase):
    def test_prediction(self):
        model = joblib.load('model.pkl')
        prediction = predict_price('model.pkl', [100, 105, 98, 10000])
        self.assertTrue(prediction > 0)

if __name__ == '__main__':
    unittest.main()