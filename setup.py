from setuptools import setup, find_packages


setup(
    name="rpp_common",
    version="0.1.0",
    description="Common RPP plugin interfaces and description types",
    packages=find_packages(include=["rpp_common", "rpp_common.*"]),
    include_package_data=True,
    install_requires=["numpy"],
)