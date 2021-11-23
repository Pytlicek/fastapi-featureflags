from fastapi_featureflags import FeatureFlags


def test_ff_1():
    ff = FeatureFlags(conf_from_json="tests/features.json")
    assert type(ff.get_features()) is dict
    assert ff.get_features() == {'json_only': False, 'ps': True, 'mam': False, 'ror': True, 'dd': True}
