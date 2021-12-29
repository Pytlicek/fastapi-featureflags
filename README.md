[![Test Python package](https://github.com/Pytlicek/fastapi-featureflags/actions/workflows/python-package.yml/badge.svg?branch=main)](https://github.com/Pytlicek/fastapi-featureflags/actions/workflows/python-package.yml) 
[![codecov](https://codecov.io/gh/Pytlicek/fastapi-featureflags/branch/main/graph/badge.svg?token=CVULQJ2SSA)](https://codecov.io/gh/Pytlicek/fastapi-featureflags) 
[![Upload Python Package to PyPI](https://github.com/Pytlicek/fastapi-featureflags/actions/workflows/python-publish.yml/badge.svg)](https://github.com/Pytlicek/fastapi-featureflags/actions/workflows/python-publish.yml) 
![PythonVersions](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue) 
[![Sourcery](https://img.shields.io/badge/Sourcery-enabled-brightgreen)](https://sourcery.ai) 
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black) 
[![Snyk](https://snyk-widget.herokuapp.com/badge/pip/sheet2dict/badge.svg)](https://snyk.io/advisor/python/fastapi-featureflags) 
[![Downloads](https://pepy.tech/badge/fastapi-featureflags)](https://pepy.tech/project/fastapi-featureflags)
[![Twitter Follow](https://img.shields.io/twitter/follow/Pytlicek?color=1DA1F2&logo=twitter&style=flat)](https://twitter.com/Pytlicek) 


# FastAPI Feature Flags

Very simple implementation of feature flags for FastAPI.  
- Minimum configuration required 
- No unnecessary dependencies
- Does its job

## Installing
To install the package from pip, first run:
```bash
pip install fastapi-featureflags
```

## Usage
A simple example of feature flags:
```
from fastapi_featureflags import FeatureFlags, feature_flag, feature_enabled

FeatureFlags(conf_from_url="https://pastebin.com/raw/4Ai3j2DC")
print("Enabled Features:", FeatureFlags.get_features())


@feature_flag("web_1")
def web_1_enabled():
    print("Feature Should be enabled: web_1")

web_1_enabled()

if feature_enabled("web_2"):
    print("Feature Should be disabled: web_2")
```

You can get FF (feature flags) from a **File**, **URL**, **Dictionary or ENV Variables**:
```
FeatureFlags.load_conf_from_url("https://pastebin.com/raw/4Ai3j2DC")
FeatureFlags.load_conf_from_json("tests/features.json")
FeatureFlags.load_conf_from_dict({"web_1": True, "web_2": False})

FeatureFlags.reload_feature_flags()
```
There is also a handler that recognizes if the "@feature_flag" wrapper is used and the flag is not registered in the config. 
This way you can also use FF at runtime. Defaults to False, so it's safer if you forget the feature flag in the code.

Function `get_features` returns a list of all registered FF  
You can enable or disable functions on the fly with `enable_feature` or `enable_feature`  

When needed you can reload all feature flags with `reload_feature_flags`, 
this is useful when you want to read and change features from URL. 
All unregistered or on-the-fly created FF, that are not in the configuration will be omitted.   

For non-production testing, a router is available, 
so you can see the paths in swagger-ui docs.
Use `include_in_schema=False` when defining the router for public deployments
```
from fastapi_featureflags import router as ff_router
app.include_router(ff_router, prefix="/ff", tags=["FeatureFlags"])
```
---
<img width="100%" alt="FastAPI-FF" src="https://user-images.githubusercontent.com/1430522/144305907-5e231e64-c120-4bde-9aad-58b9b194a361.png">

# Contributing and Code of Conduct  
### Contributing to fastapi-featureflags  
As an open source project, fastapi-featureflags welcomes contributions of many forms.  
Please read and follow our [Contributing to fastapi-featureflags](CONTRIBUTING.md)  

### Code of Conduct  
As a contributor, you can help us keep the fastapi-featureflags project open and inclusive.  
Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md)  
