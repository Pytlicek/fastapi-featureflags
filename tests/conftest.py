import pytest
import sys
from pathlib import Path

sys.path.append(str(Path(".").absolute().parent))

from fastapi_featureflags import FeatureFlags


@pytest.fixture(scope="module")
def featureflags():
    return FeatureFlags()
