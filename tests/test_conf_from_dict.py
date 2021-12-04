import os
import ast


def test_ff_from_dict(featureflags):
    featureflags.load_conf_from_dict(
        {
            "json_only": False,
            "file_1": True,
            "file_2": False,
            "file_3": True,
            "file_4": True,
        }
    )

    assert type(featureflags.get_features()) is dict
    assert featureflags.conf_from_dict is not None

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


def test_ff_from_env(featureflags):
    env_variable = ast.literal_eval(os.getenv("FASTAPI_FF", {}))
    featureflags.load_conf_from_dict(env_variable)
    assert type(featureflags.get_features()) is dict
    assert featureflags.get_features() == {
        "json_only": False,
        "file_1": True,
        "file_2": False,
        "file_3": True,
        "file_4": True,
    }

    featureflags.enable_feature("json_only")
    assert featureflags.get_features()["json_only"] is True

    action = featureflags.reload_feature_flags()
    assert action is True
    assert featureflags.get_features()["json_only"] is False


def test_ff_from_env_na(featureflags):
    env_variable = ast.literal_eval(os.getenv("FASTAPI_FF_NON_EXISTING", "{}"))
    featureflags.load_conf_from_dict(env_variable)
    assert type(featureflags.get_features()) is dict
    assert featureflags.get_features() == {}
