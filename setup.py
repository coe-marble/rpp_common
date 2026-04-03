from setuptools import setup


setup(
    name="rpp_common",
    version="0.1.0",
    description="Common RPP plugin interfaces and description types",
    packages=["rpp_common", "rpp_common.py"],
    package_dir={
        "rpp_common": "rpp_common",
        "rpp_common.py": "rpp_common/py",
    },
    include_package_data=True,
    install_requires=["numpy"],
)