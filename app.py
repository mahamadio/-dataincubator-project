from flask import Flask,render_template
from flask import jsonify
import requests
from flask import request


API_KEY = 'NUV3434542P4MA0T'

app  = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/getJSONDATA/', methods=[ 'GET','POST'])
def summary():
    print(request.form,flush=True)
    app.logger.info('Processing default request')
    symbol = request.form.get('symbol')
    monthly = request.form.get('monthly')
    weakly = request.form.get('weakly')
    daily = request.form.get('daily')
    min_interval = request.form.get('min_interval')
    
    print('#############################')
    print(symbol,flush=True)
    print(monthly,flush=True)
    print(weakly,flush=True)
    print(daily,flush=True)
    print(min_interval,flush=True) 
    print('#############################')

    if monthly == 'on':
        print('monthely')
        response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={}&apikey={}'.format(symbol,API_KEY))
        jsonResponse = response.json()
        print(jsonResponse)
    elif weakly == 'on':
        print('weakely')
        response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={}&apikey={}'.format(symbol,API_KEY))
        jsonResponse = response.json()
        print(jsonResponse)            
    elif daily == 'on':
        print('daily')
        response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey={}'.format(symbol,API_KEY))
        jsonResponse = response.json()
        print(jsonResponse)            
    elif min_interval != '':
        print('min_interval',min_interval)
        response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={}&interval={}min&apikey={}'.format(symbol,min_interval,API_KEY))
        jsonResponse = response.json()
        print(jsonResponse)   
    else:
        response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=IBM&apikey={}'.format(symbol,API_KEY))
        jsonResponse = response.json()
        print(jsonResponse)   
     
    return jsonify(jsonResponse)


if __name__ == '__main__':
    app.run(debug=True)


