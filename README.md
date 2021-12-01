# FastAPI Feature Flags

Very simple implementation of feature flags for FastAPI.  
- Minimum configuration required. 
- No unnecessary dependencies
- Does its job

## Installing
To install the package from pip, first run:
```bash
pip install -U https://github.com/Pytlicek/fastapi-featureflags/archive/refs/tags/0.0.1.zip
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

You can get FF (feature flags) from a file or URL:
```
FeatureFlags.load_conf_from_url("https://pastebin.com/raw/4Ai3j2DC")
FeatureFlags.load_conf_from_json("tests/features.json")

FeatureFlags.reload_feature_flags()
```
There is also a handler that recognizes if the "@feature_flag" wrapper is used and the flag is not registered in the config. 
This way you can also use FF at runtime. Defaults to False, so it's safer if you forget the feature flag in the code.

Function `get_features` returns a list of all registered FF  
You can enable or disable functions on the fly with `enable_feature` or `enable_feature`  

When needed you can reload all feature flags with `reload_feature_flags`, 
this is handy when you want to read and change features from URL fe.

For non-production testing, a router is available, 
so you can see the paths in swagger-ui docs.
Use `include_in_schema=False` when defining the router for public deployments
```
from fastapi_featureflags import router as ff_router
app.include_router(ff_router)
```

### TODO
- Tests
- Better rewrite of the main class 
- Packaging
- FF from environments
