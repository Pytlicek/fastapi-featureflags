from fastapi_featureflags import FeatureFlags, feature_enabled


def test_empty_config():
    empty_ff = FeatureFlags.reload_feature_flags()
    assert type(empty_ff) is bool


def test_config_from_dict(featureflags):
    conf_from_dict = featureflags.load_conf_from_dict(
        {
            "dict_only": False,
            "feat_1": True,
            "feat_2": False,
            "feat_3": True,
            "feat_4": True,
        }
    )
    assert type(conf_from_dict) is bool


def test_reload_ff(featureflags, ff_from_dict):
    reload_ff = featureflags.reload_feature_flags()
    assert type(reload_ff) is bool

    reload_ff = ff_from_dict.reload_feature_flags()
    assert type(reload_ff) is bool


def test_get_features(ff_from_dict):
    get_features = ff_from_dict.get_features()
    assert type(get_features) is dict


def test_is_enabled(ff_from_dict):
    is_enabled = ff_from_dict.is_enabled("dict_only")
    assert type(is_enabled) is bool

    is_enabled = ff_from_dict.is_enabled("non-existent")
    assert type(is_enabled) is bool


def test_enable_feature(ff_from_dict):
    enable_feature = ff_from_dict.enable_feature("dict_only")
    assert type(enable_feature) is bool

    enable_feature = ff_from_dict.enable_feature("non-existent")
    assert type(enable_feature) is bool


def test_disable_feature(ff_from_dict):
    disable_feature = ff_from_dict.disable_feature("dict_only")
    assert type(disable_feature) is bool

    disable_feature = ff_from_dict.disable_feature("non-existent")
    assert type(disable_feature) is bool


def test_feature_enabled():
    is_feature_enabled = feature_enabled("dict_only")
    assert type(is_feature_enabled) is bool

    is_feature_enabled = feature_enabled("non-existent")
    assert type(is_feature_enabled) is bool


def test_config_from_json(featureflags):
    conf_from_json = featureflags.load_conf_from_json("tests/features.json")
    assert type(conf_from_json) is bool


def test_config_from_url(featureflags):
    conf_from_url = featureflags.load_conf_from_url("https://pastebin.com/raw/4Ai3j2DC")
    assert type(conf_from_url) is bool
