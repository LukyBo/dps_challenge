# %% Import libraries
import json
from flask import Flask, request, jsonify
import pickle


app = Flask(__name__)
with open('forecast_model.pckl', 'rb') as fin:
    m2 = pickle.load(fin)
@app.route("/predict", methods=['POST'])
def predict():
    
    year = int(request.json['year'])    
    month = int(request.json['month'])
    horizon = month*(year%10)
    future2 = m2.make_future_dataframe(periods=horizon,freq='30d' )
    forecast2 = m2.predict(future2)
    
    data = forecast2['yhat'][-1:]
    ret = json.dumps(data, default=float)

    return jsonify({'prediction':float(ret)})# running REST interface, port=3000 for direct test
if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=3000)



