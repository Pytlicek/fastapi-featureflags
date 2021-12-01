from . import FeatureFlags
from fastapi import APIRouter

router = APIRouter()


@router.get("/all")
def show_feature_flags():
    """
    Return all feature flags
    :return: string
    """
    return FeatureFlags.get_features()


@router.get("/enable/{feature_flag}")
def enable_feature_flag(feature_flag: str):
    """
    Enable feature flag
    :return: json
    """
    feature_status = FeatureFlags.enable_feature(feature_flag)
    return {"feature_flag": feature_flag, "enabled": feature_status}


@router.get("/disable/{feature_flag}")
def disable_feature_flag(feature_flag: str):
    """
    Disable feature flag
    :return: json
    """
    feature_status = FeatureFlags.disable_feature(feature_flag)
    return {"feature_flag": feature_flag, "enabled": feature_status}


@router.get("/reload")
def reload_feature_flags():
    """
    Reload feature flags from last loaded configuration
    :return: json
    """
    reload_status = FeatureFlags.reload_feature_flags()
    return {"feature_flags": FeatureFlags.get_features(), "reloaded": reload_status}
