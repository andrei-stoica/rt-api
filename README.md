# RiskThinking.AI work sample API

Andrei Stoica<br>
May 23, 2023

## Setup

Install dependencies
```sh
pip install -r requirements.txt
```

Run development server 
```sh
flask run --debug
```

To run production server
```
gunicorn app:app
```
A version of this site is hosted at [https://rt-ws.andreistoica.ca/predict](https://rt-ws.andreistoica.ca/predict?vol_moving_avg=12345&adj_close_rolling_med=25)