import sys
from pathlib import Path

import pytest

from fastapi_featureflags import FeatureFlags

sys.path.append(str(Path(".").absolute().parent))


@pytest.fixture(scope="module")
def featureflags():
    return FeatureFlags


@pytest.fixture(scope="module")
def ff_from_dict(featureflags):
    featureflags.load_conf_from_dict(
        {
            "dict_only": False,
            "file_1": True,
            "file_2": False,
            "file_3": True,
            "file_4": True,
        }
    )
    return FeatureFlags
