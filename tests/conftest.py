import sys
from pathlib import Path

import pytest

from fastapi_featureflags import FeatureFlags

sys.path.append(str(Path(".").absolute().parent))


@pytest.fixture(scope="module")
def featureflags():
    return FeatureFlags
