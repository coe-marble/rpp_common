from setuptools import setup


setup(
    name="rpp_common",
    version="0.1.0",
    description="Common RPP plugin interfaces and description types",
    packages=[
        "rpp_common",
        "rpp_common.py",
        "rpp_common.common_plugins",
    ],
    package_dir={
        "rpp_common": "rpp_common",
        "rpp_common.py": "rpp_common/py",
        "rpp_common.common_plugins": "rpp_common/common_plugins",
    },
    package_data={
        "rpp_common": ["py.typed", "__init__.pyi"],
    },
    include_package_data=True,
    install_requires=["numpy"],
)