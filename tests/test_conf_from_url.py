from fastapi_featureflags import feature_enabled


def test_ff_from_url(featureflags):
    featureflags.load_conf_from_url("https://pastebin.com/raw/4Ai3j2DC")

    assert type(featureflags.get_features()) is dict
    assert featureflags.conf_from_url is not None

    assert featureflags.get_features() == {
        "web_only": False,
        "web_1": True,
        "web_2": False,
        "web_3": True,
        "web_4": False,
    }


def test_enable_feature(featureflags):
    assert featureflags.get_features()["web_only"] is False
    action = featureflags.enable_feature("web_only")
    assert action is True
    assert featureflags.get_features()["web_only"] is True


def test_disable_feature(featureflags):
    assert featureflags.get_features()["web_1"] is True
    action = featureflags.disable_feature("web_1")
    assert action is False
    assert featureflags.get_features()["web_1"] is False


def test_feature_enabled(featureflags):
    assert featureflags.get_features()["web_4"] is False
    assert feature_enabled("web_4") is False
    assert featureflags.is_enabled("web_4") is False
    featureflags.enable_feature("web_4")
    assert feature_enabled("web_4") is True
    assert featureflags.is_enabled("web_4") is True


def test_reload_features(featureflags):
    assert featureflags.get_features()["web_only"] is True
    assert featureflags.get_features()["web_1"] is False
    action = featureflags.reload_feature_flags()
    assert action is True
    assert featureflags.get_features()["web_only"] is False
    assert featureflags.get_features()["web_1"] is True
