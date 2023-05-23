from flask import Flask, request, abort
from os import path, environ, listdir
from catboost import CatBoostRegressor

app = Flask(__name__)
PORT = int(environ.get("PORT", 8080))


data_dir = environ.get("MODEL_DIR", "models")
print(data_dir)
models = listdir(data_dir)
models.sort()

model = CatBoostRegressor()
model.load_model(path.join(data_dir, models[-1]))


@app.route("/")
def index():
    return """
    <head> </head>
    <body>
    <h1>Hello World</h1>
    <p> please use <a href='/predict'>/predict?vol_moving_avg=&lt;VOLUME&gt;&adj_close_rolling_med=&lt;CLOSE&gt;</a>
    </body>
    """


@app.route("/predict")
def predict():
    vol = request.args.get("vol_moving_avg")
    close = request.args.get("adj_close_rolling_med")
    try:
        vol = int(vol)
        close = int(close)
    except (ValueError, TypeError) as e:
        abort(400, description="Missing or malformed parmeters")

    print(type(vol), vol)
    print(type(close), close)

    return str(int(model.predict([vol, close])))


if __name__ == "__main__":
    app.run(port=PORT)
