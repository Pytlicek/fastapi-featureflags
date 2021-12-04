def test_ff_from_json(featureflags):
    featureflags.load_conf_from_json("tests/features.json")

    assert type(featureflags.get_features()) is dict
    assert featureflags.conf_from_json is not None

    assert featureflags.get_features() == {
        "json_only": False,
        "file_1": True,
        "file_2": False,
        "file_3": True,
        "file_4": True,
    }


def test_reload_features(featureflags):
    assert featureflags.get_features()["json_only"] is False
    assert featureflags.get_features()["file_1"] is True

    featureflags.enable_feature("json_only")
    featureflags.disable_feature("file_1")
    assert featureflags.get_features()["json_only"] is True
    assert featureflags.get_features()["file_1"] is False

    action = featureflags.reload_feature_flags()
    assert action is True
    assert featureflags.get_features()["json_only"] is False
    assert featureflags.get_features()["file_1"] is True
