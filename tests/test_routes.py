from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi_featureflags import router as ff_router

app = FastAPI()
app.include_router(ff_router, prefix="/ff", tags=["FeatureFlags"])
client = TestClient(app)


def test_openapi_json(featureflags):
    response = client.get("/openapi.json")
    assert response.status_code == 200
    assert "/all" in response.text


def test_create_ff(featureflags):
    featureflags.load_conf_from_url("https://pastebin.com/raw/4Ai3j2DC")
    assert featureflags.get_features() == {
        "web_only": False,
        "web_1": True,
        "web_2": False,
        "web_3": True,
        "web_4": False,
    }


def test_routes_all():
    response = client.get("/ff/all")
    assert response.status_code == 200
    assert response.json() == {
        "web_only": False,
        "web_1": True,
        "web_2": False,
        "web_3": True,
        "web_4": False,
    }


def test_routes_enable_ff():
    response = client.get("/ff/enable/web_only")
    assert response.status_code == 200
    assert response.json() == {"feature_flag": "web_only", "enabled": True}

    response = client.get("/ff/all")
    assert response.status_code == 200
    assert response.json()["web_only"] is True


def test_routes_disable_ff():
    response = client.get("/ff/disable/web_1")
    assert response.status_code == 200
    assert response.json() == {"feature_flag": "web_1", "enabled": False}

    response = client.get("/ff/all")
    assert response.status_code == 200
    assert response.json()["web_1"] is False


def test_routes_reload_ff():
    response = client.get("/ff/reload")
    assert response.status_code == 200
    assert response.json() == {
        "feature_flags": {
            "web_only": False,
            "web_1": True,
            "web_2": False,
            "web_3": True,
            "web_4": False,
        },
        "reloaded": True,
    }

    response = client.get("/ff/all")
    assert response.status_code == 200
    assert response.json()["web_1"] is True


app = FastAPI()
app.include_router(
    ff_router, prefix="/ff", tags=["FeatureFlags"], include_in_schema=False
)
client_wo_schema = TestClient(app)


def test_schema_without_routes():
    response = client_wo_schema.get("/openapi.json")
    assert response.status_code == 200
    assert "/all" not in response.text
    assert response.json()["paths"] == {}
