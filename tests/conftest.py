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
            "feat_1": True,
            "feat_2": False,
            "feat_3": True,
            "feat_4": True,
        }
    )
    return FeatureFlags
