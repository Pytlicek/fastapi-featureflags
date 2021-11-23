import json
import requests


class FeatureFlags(object):
    features = {}

    def __init__(
            self,
            conf_from_json: str = "",
            conf_from_url: str = "",
            **kwargs,
    ):
        self.handle_config(conf_from_json, conf_from_url)

    def handle_config(self, conf_from_json, conf_from_url):
        if conf_from_json:
            with open(conf_from_json, "r") as f:
                params = json.loads(f.read())
                for k, v in params.items():
                    self.features[k] = v
        elif conf_from_url:
            params = requests.get(conf_from_url).json()
            print(params)
            for k, v in params.items():
                self.features[k] = v

    @classmethod
    def handle_feature(cls, feature_name):
        features = cls.features
        if features.get(feature_name, False) is False:
            features[feature_name] = False

    @classmethod
    def is_enabled(cls, feature_name):
        features = cls.features
        return features.get(feature_name, False)

    @classmethod
    def get_features(cls):
        return cls.features

    @classmethod
    def enable_feature(cls, feature_name):
        cls.features[feature_name] = True
        return cls.features[feature_name]

    @classmethod
    def disable_feature(cls, feature_name):
        cls.features[feature_name] = False
        return cls.features[feature_name]


def feature_flag(feature_name):
    def decorator(function):
        def wrapper(*args, **kwargs):
            FeatureFlags.handle_feature(feature_name)
            if FeatureFlags.is_enabled(feature_name):
                # print("Feature Enabled:", feature_name)
                return function(*args, **kwargs)
            else:
                # print("Feature Disabled:", feature_name)
                return True

        return wrapper

    return decorator


def feature_enabled(feature_name):
    FeatureFlags.handle_feature(feature_name)
    return FeatureFlags.is_enabled(feature_name)
