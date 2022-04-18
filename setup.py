import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fastapi_featureflags",
    version="0.4.6",
    author="Tomas Pytel",
    author_email="pytlicek@gmail.com",
    description="Feature Flags for FastAPI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Pytlicek/fastapi-featureflags",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests", "fastapi"],
    python_requires=">=3.6",
)
