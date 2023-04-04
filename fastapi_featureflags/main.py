import json
import requests


class FeatureFlags(object):
    """
    A class representing feature flags.

    Attributes:
        conf_from_json (str): The path to the JSON file containing the feature flags configuration.
        conf_from_url (str): The URL of the JSON file containing the feature flags configuration.
        conf_from_dict (dict): A dictionary containing the feature flags configuration.
        features (dict): A dictionary containing the feature flags and their values.
    """

    conf_from_json = None
    conf_from_url = None
    conf_from_dict = None
    features = {}

    @staticmethod
    def load_conf_from_url(conf_from_url: str) -> bool:
        """
        Load feature flags configuration from a JSON file at a given URL.

        Args:
            conf_from_url (str): The URL of the JSON file containing the feature flags configuration.

        Returns:
            bool: True if the configuration was loaded successfully, False otherwise.
        """
        FeatureFlags.features.clear()
        FeatureFlags.conf_from_url = conf_from_url
        params = requests.get(conf_from_url).json()
        for k, v in params.items():
            FeatureFlags.features[k] = v
        return True

    @staticmethod
    def load_conf_from_json(conf_from_json: str) -> bool:
        """
        Load feature flags configuration from a JSON file at a given path.

        Args:
            conf_from_json (str): The path to the JSON file containing the feature flags configuration.

        Returns:
            bool: True if the configuration was loaded successfully, False otherwise.
        """
        FeatureFlags.features.clear()
        FeatureFlags.conf_from_json = conf_from_json
        with open(conf_from_json, "r") as f:
            params = json.loads(f.read())
            for k, v in params.items():
                FeatureFlags.features[k] = v
        return True

    @staticmethod
    def load_conf_from_dict(conf_from_dict: dict) -> bool:
        """
        Load feature flags configuration from a dictionary.

        Args:
            conf_from_dict (dict): A dictionary containing the feature flags configuration.

        Returns:
            bool: True if the configuration was loaded successfully, False otherwise.
        """
        FeatureFlags.features.clear()
        FeatureFlags.conf_from_dict = conf_from_dict
        for k, v in conf_from_dict.items():
            FeatureFlags.features[k] = v
        return True

    @staticmethod
    def reload_feature_flags() -> bool:
        """
        Reload the feature flags configuration from the original source.

        Returns:
            bool: True if the configuration was reloaded successfully, False otherwise.
        """
        FeatureFlags.features.clear()
        if FeatureFlags.conf_from_url:
            FeatureFlags.load_conf_from_url(FeatureFlags.conf_from_url)
            return True
        elif FeatureFlags.conf_from_json:
            FeatureFlags.load_conf_from_json(FeatureFlags.conf_from_json)
            return True
        elif FeatureFlags.conf_from_dict:
            FeatureFlags.load_conf_from_dict(FeatureFlags.conf_from_dict)
            return True
        else:
            return False

    @classmethod
    def handle_feature(cls, feature_name: str):
        """
        Add a feature flag to the dictionary of feature flags if not exist.

        Args:
            feature_name (str): The name of the feature flag.
        """
        features = cls.features
        if features.get(feature_name, False) is False:
            features[feature_name] = False

    @classmethod
    def get_features(cls) -> dict:
        """
        Get the dictionary of feature flags.

        Returns:
            dict: A dictionary containing the feature flags
        """
        return cls.features

    @classmethod
    def is_enabled(cls, feature_name: str) -> bool:
        """Check if a given feature is enabled.

        Args:
            feature_name (str): The name of the feature to check.

        Returns:
            bool: True if the feature is enabled, False otherwise.
        """
        features = cls.features
        return features.get(feature_name, False)

    @classmethod
    def enable_feature(cls, feature_name: str) -> bool:
        """Enable a given feature.

        Args:
            feature_name (str): The name of the feature to enable.

        Returns:
            bool: True if the feature was successfully enabled, False otherwise.
        """
        cls.features[feature_name] = True
        return cls.features[feature_name]

    @classmethod
    def disable_feature(cls, feature_name: str) -> bool:
        """Disable a given feature.

        Args:
            feature_name (str): The name of the feature to disable.

        Returns:
            bool: True if the feature was successfully disabled, False otherwise.
        """
        cls.features[feature_name] = False
        return cls.features[feature_name]


def feature_flag(feature_name: str):
    """A decorator that can be used to specify a feature flag for a function.

    This decorator checks if a feature is enabled before executing a function. If the feature
    is not enabled, the function is skipped.

    Args:
        feature_name (str): The name of the feature to check.

    Returns:
        function: The decorated function, or a function that always returns True if the
            feature is not enabled.
    """

    def decorator(function):
        def wrapper(*args, **kwargs):
            FeatureFlags.handle_feature(feature_name)
            if FeatureFlags.is_enabled(feature_name):
                return function(*args, **kwargs)
            else:
                return True

        return wrapper

    return decorator


def feature_enabled(feature_name: str) -> bool:
    """Check if a given feature is enabled.

    This function is similar to the `is_enabled` method of the `FeatureFlags` class, but it
    does not track the feature if it is not already tracked.

    Args:
        feature_name (str): The name of the feature to check.

    Returns:
        bool: True if the feature is enabled, False otherwise.
    """
    FeatureFlags.handle_feature(feature_name)
    return FeatureFlags.is_enabled(feature_name)
