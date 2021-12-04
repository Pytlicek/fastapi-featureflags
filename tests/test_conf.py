from fastapi_featureflags import FeatureFlags, feature_flag


def test_empty_config():
    empty_ff = FeatureFlags
    reload_result = empty_ff.reload_feature_flags()
    assert reload_result is False

    assert empty_ff.conf_from_dict is None
    assert empty_ff.conf_from_json is None
    assert empty_ff.conf_from_url is None


def test_feature_flag_wrapper(featureflags):
    assert featureflags.get_features().get("non_existing", None) is None

    @feature_flag("non_existing")
    def my_non_registered_feature():
        return False

    ff_call_result = my_non_registered_feature()
    assert featureflags.get_features()["non_existing"] is False
    assert ff_call_result is True

    featureflags.enable_feature("non_existing")
    assert featureflags.get_features()["non_existing"] is True
    assert my_non_registered_feature() is False
