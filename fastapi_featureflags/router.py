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
