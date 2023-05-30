import sys

sys.path += ["."]

import pytest
import app as rt_api


@pytest.fixture()
def app():
    return rt_api.app


@pytest.fixture()
def model():
    return rt_api.model


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_request(client, model):
    vol = 12345
    close = 25
    expected_value = int(model.predict([vol, close]))

    resp = client.get(f"/predict?vol_moving_avg={vol}&adj_close_rolling_med={close}")
    assert int(resp.text) == expected_value

    resp = client.get("/predict")
    assert resp.status_code == 400
